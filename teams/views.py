from rest_framework import viewsets, permissions
from .models import Team
from .serializers import TeamSerializer
from rest_framework.response import Response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        team = serializer.save(owner=self.request.user)
        team.members.add(self.request.user)
