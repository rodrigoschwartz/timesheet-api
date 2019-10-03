from django.db import models
from core.models import Project

# Create your models here.


class Hours(models.Model):
    id = models.IntegerField(primary_key=True)
    hours = models.IntegerField(default=0, help_text="Enter a project hours") 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # responsible =
    created_at = models.DateTimeField(auto_now_add=True)