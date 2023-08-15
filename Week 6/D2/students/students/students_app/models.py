from django.db import models
from django.utils import timezone


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)


def __str__(self):
    return f"{self.first_name} {self.last_name}"
