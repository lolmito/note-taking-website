from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView): #ListCreateAPIView - list all the notes the user has created or create a new note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user #returns the authenticated user
        return Note.objects.filter(author=user) #gets all notes written by the user
    
    def perform_create(self, serializer): #custom function for adding functionality, such as adding new arguments/fields
        if serializer.is_valid():
            serializer.save(author=self.request.user) #author=self.request.user is an additional field added to the note, since author field in serializer is a addt'l kwargs
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # specifying all the different objects in the user
    serializer_class = UserSerializer #what data is needed to make a new user
    permission_classes = [AllowAny] # who is allowed to create a user
