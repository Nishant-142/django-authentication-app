from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_admin_user = models.BooleanField(default=False)
    is_normal_user = models.BooleanField(default = True)
