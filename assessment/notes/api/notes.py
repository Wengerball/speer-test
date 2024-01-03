from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.models import User
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(
            Q(owner=user) | Q(shared_with=user)).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {'message': 'Note deleted successfully.'},
                status=status.HTTP_200_OK)
        except Http404:
            return Response(
                {'error': 'Note not found.'},
                status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['POST'])
    def share(self, request, pk=None):
        note = self.get_object()
        recipient_username = request.data.get('shared_with')
        print(recipient_username)

        # Check if the recipient user exists
        try:
            recipient_user = User.objects.get(username=recipient_username)
        except User.DoesNotExist:
            return Response(
                {'error': 'Recipient user not found.'},
                status=status.HTTP_404_NOT_FOUND)

        # Check if the note is already shared with the recipient
        if note.shared_with.filter(username=recipient_username).exists():
            return Response(
                {'error': 'Note is already shared with the recipient.'},
                status=status.HTTP_400_BAD_REQUEST)

        # Share the note with the recipient user
        note.shared_with.add(recipient_user)
        return Response(
            {'message': 'Note shared successfully.'},
            status=status.HTTP_200_OK)


class NoteSearch(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q')
        if query:
            notes = Note.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                Q(owner=request.user) | Q(shared_with=request.user)
            ).distinct()
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {'message': 'No query provided'},
                status=status.HTTP_400_BAD_REQUEST)
