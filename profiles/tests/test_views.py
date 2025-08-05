from django.contrib.auth.models import User
from django.test.utils import override_settings
from django.urls import reverse
import pytest

from profiles.models import Profile


@pytest.fixture
def test_profile():
    """Fixture providing a saved Profile instance."""
    return Profile.objects.create(
        user=User.objects.create_user(username="Bart", password="el_barto666"),
        favorite_city="Springfield"
    )


@pytest.mark.django_db
@override_settings(SECRET_KEY="secret-test-key")
def test_profile_idex_view(client, test_profile):
    """ Test that the profile index view returns a 200 status code and the correct template. """
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert test_profile.user.username in response.content.decode()


@pytest.mark.django_db
@override_settings(SECRET_KEY="secret-test-key")
def test_profile_view(client, test_profile):
    """ Test that the profile view returns a 200 status code and the correct template. """
    url = reverse('profiles:profile', kwargs={'username': test_profile.user.username})
    response = client.get(url)
    assert response.status_code == 200
    assert test_profile.user.username in response.content.decode()


@pytest.mark.django_db
@override_settings(DEBUG=False, ALLOWED_HOSTS=["*"], SECRET_KEY="secret-test-key")
def test_profile_view_404_error(client):
    """ Test that the profile view returns a 404 status code when the profile is not found. """
    url = reverse('profiles:profile', kwargs={'username': "Bart"})
    response = client.get(url)
    assert response.status_code == 404
