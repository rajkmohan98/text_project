# notes/urls.py
from django.urls import path
from .views import NoteCreateAPIView, NoteListAPIView

urlpatterns = [
    path('note/', NoteCreateAPIView.as_view(), name='note_create'),
    path('notes/', NoteListAPIView.as_view(), name='note_list'),  # For GET requests
]
