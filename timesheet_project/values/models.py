from django.db import models
from core.models import Project

# Create your models here.

class Values(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.DecimalField(
        decimal_places=2, max_digits=20, help_text="Enter a project value")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # responsible =
    created_at = models.DateTimeField(auto_now_add=True)
    # attchment 