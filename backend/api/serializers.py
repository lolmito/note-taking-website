from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#Object Relational Mapping
#JSON is the standard format when communicating with web applications
#Convert JSON data to python data and vice versa

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}