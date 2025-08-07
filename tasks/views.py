from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(project__team__members=user)

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if self.request.user == project.team.owner:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Sadece proje sahibi görev oluşturabilir.")
