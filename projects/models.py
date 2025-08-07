from django.db import models
from teams.models import Team

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title
