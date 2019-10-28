from django.db import models
from core.models import Project
from django.contrib.auth.models import User

# Create your models here.
class Hours(models.Model):
    id = models.AutoField(primary_key=True)
    hours = models.IntegerField(default=0) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)