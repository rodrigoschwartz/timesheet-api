from django.db import models
from core.models import Project
from django.contrib.auth.models import User

GASTO = (
    ("1", "Alimentação"),
    ("2", "Estadia"),
    ("3", "Transporte"),
    ("4", "Outros")
)

class Values(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.DecimalField(decimal_places=2, max_digits=20)
    type =  models.CharField(
        max_length=2,
        choices=GASTO,
        blank=True,
        default="1",
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

