from django.test import TestCase
from notes.serializers import NoteSerializer


class NoteSerializerTestCase(TestCase):
    def test_note_serializer_valid(self):
        data = {'title': 'Test Note', 'content': 'This is a test note.'}
        serializer = NoteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_note_serializer_invalid(self):
        data = {'title': 'Test Note'}
        serializer = NoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())
