from django.urls import reverse
from django.test.utils import override_settings
import pytest

from lettings.models import Letting, Address


@pytest.fixture
def test_address():
    """Fixture providing a saved Address instance."""
    return Address.objects.create(
        number=123,
        street="Private street",
        city="Private city",
        state="TS",
        zip_code=12345,
        country_iso_code="TST"
    )


@pytest.fixture
def test_letting(test_address):
    """Fixture providing a saved Letting instance."""
    return Letting.objects.create(
        title="Test Letting",
        address=test_address
    )


@pytest.mark.django_db
def test_lettings_index_view(client, test_letting):
    """ Test that the lettings index view returns a 200 status code and the correct template. """
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert test_letting.title in response.content.decode()


@pytest.mark.django_db
def test_lettings_letting_view(client, test_letting):
    """ Test that the letting view returns a 200 status code and the correct template. """
    url = reverse('lettings:letting', kwargs={'letting_id': test_letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assert test_letting.address.street in response.content.decode()


@override_settings(DEBUG=False, ALLOWED_HOSTS=["*"])
@pytest.mark.django_db
def test_lettings_letting_view_not_found(client):
    """ Test that the letting view returns a 404 status code when the letting is not found. """
    url = reverse('lettings:letting', kwargs={'letting_id': "999"})
    response = client.get(url)
    assert response.status_code == 404
