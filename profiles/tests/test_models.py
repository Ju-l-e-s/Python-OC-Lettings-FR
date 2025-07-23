"""
Tests for the profiles application models.

This module contains test cases that verify the behavior of the Profile model,
including string representation and model relationships.
"""

from django.contrib.auth.models import User
from django.db import IntegrityError
import pytest

from profiles.models import Profile


@pytest.fixture
def test_user():
    """Fixture providing a saved User instance."""
    return User.objects.create_user(username='jules', password='pass')


@pytest.fixture
def test_profile(test_user):
    """Fixture providing a saved Profile instance."""
    return Profile.objects.create(user=test_user, favorite_city='Bordeaux')


@pytest.mark.django_db
def test_str_profile(test_profile):
    """__str__ must return the username of the linked User."""
    assert str(test_profile) == test_profile.user.username


@pytest.mark.django_db
def test_one_to_one_uniqueness(test_user):
    """
    A User cannot have two Profile instances.
    Should raise IntegrityError on second creation.
    """
    Profile.objects.create(user=test_user)
    with pytest.raises(IntegrityError):
        Profile.objects.create(user=test_user)


@pytest.mark.django_db
def test_cascade_delete_user(test_user):
    """
    Deleting a User should delete the associated Profile (CASCADE).
    """
    test_user.delete()
    assert not Profile.objects.filter(user_id=test_user.id).exists()
