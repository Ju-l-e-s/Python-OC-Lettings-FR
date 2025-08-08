"""Data models for the profiles application.

This module defines the database models used in the profiles application,
including Profile model.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Represents a user profile.

    Attributes:
        user (User): The user linked to the profile.
            One-to-one relationship with the User model. Deleted if the user is deleted.
        favorite_city (str): The favorite city of the profile.
            Maximum length of 64 characters.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'oc_lettings_site_profile'

    def __str__(self):
        return self.user.username
