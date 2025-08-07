from rest_framework import serializers
from .models import Project
from teams.models import Team

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'is_active', 'team']
