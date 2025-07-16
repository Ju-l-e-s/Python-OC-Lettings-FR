from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model.

    Attributes:
        user (User): The user of the profile.
        favorite_city (str): The favorite city of the profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
