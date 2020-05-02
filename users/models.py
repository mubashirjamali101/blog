from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    # other fields
    accepted_eula = models.BooleanField()