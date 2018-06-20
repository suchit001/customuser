from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    gender = models.CharField(max_length=6)
    phone_no = models.IntegerField(default=False)
    sq = models.IntegerField(default=False)

    def __str__(self):
        return self.email