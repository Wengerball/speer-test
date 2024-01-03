from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from notes.models import Note


class NoteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.note_data = {'title': 'Test Note',
                          'content': 'This is a test note.'}
        self.note = Note.objects.create(owner=self.user, **self.note_data)

    def test_get_all_notes(self):
        url = reverse('note-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_by_id(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_note(self):
        url = reverse('note-list')
        response = self.client.post(url, self.note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_note(self):
        url = reverse('note-detail', args=[self.note.id])
        updated_data = {'title': 'Updated Note',
                        'content': 'This is an updated test note.'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note(self):
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
