from django.db import models
from core.models import Project
from django.contrib.auth.models import User


class Values(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.DecimalField(decimal_places=2, max_digits=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # attchment

