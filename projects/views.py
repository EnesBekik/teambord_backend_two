from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Sadece üyesi olduğu takımların projeleri
        user = self.request.user
        return Project.objects.filter(team__members=user)

    def perform_create(self, serializer):
        # Oluşturan kişi takıma dahilse eklesin
        team = serializer.validated_data['team']
        if self.request.user in team.members.all():
            serializer.save()
        else:
            raise permissions.PermissionDenied("Bu takıma proje ekleyemezsin.")
