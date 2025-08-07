from rest_framework import serializers
from .models import Team
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TeamSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'owner', 'members']
