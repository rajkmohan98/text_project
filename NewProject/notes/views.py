from rest_framework.views import APIView
from rest_framework.response import Response
from notes.models import Notes_table
from notes.serializer import NoteSerializer
from rest_framework import status

class NoteCreateAPIView(APIView):
    def post(self, request):
        serializer = NoteSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response({"message": "Notes created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteListAPIView(APIView):
    def get(self, request):
        instances = Notes_table.objects.all()
        serializer = NoteSerializer(instances, many=True)  # Use NoteSerializer for serialization
        return Response(serializer.data)
