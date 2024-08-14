
from rest_framework import serializers
from notes.models import Notes_table

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes_table
        fields = ['user_name', 'text_content']
