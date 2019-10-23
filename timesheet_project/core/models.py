from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    ("1", "Planning"),
    ("2", "Execution"),
    ("3", "Tests"),
    ("4", "Go Live"),
    ("5", "Finished"),
)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    demandCode = models.IntegerField()
    description = models.CharField(max_length=60)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    value = models.DecimalField( decimal_places=2, max_digits=20 )
    hoursAp = models.IntegerField(default=0)
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        blank=True,
        default="1",
    )

    def __str__(self):
        return self.description
