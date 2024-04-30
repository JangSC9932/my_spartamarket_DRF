from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True)
    birthday = models.DateField()
    introduction = models.TextField(null=True)
