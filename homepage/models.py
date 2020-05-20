from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)
    # https://stackoverflow.com/questions/15988183/cant-create-super-user-with-custom-user-model-in-django-1-5
    age = models.IntegerField(null=True)