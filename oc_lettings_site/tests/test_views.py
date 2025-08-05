import oc_lettings_site.urls as urls_module
from django.urls import reverse
from django.test import Client, override_settings
import pytest


@pytest.mark.django_db
def test_index_view(client):
    """ Test that the index view returns a 200 status code and the correct template """
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()


@pytest.mark.django_db
@override_settings(DEBUG=False, ALLOWED_HOSTS=['*'])
def test_404_error_handling(client):
    """ Test that the 404 error view returns a 404 status code and the correct template """
    response = client.get("/bad_url")
    assert response.status_code == 404
    content = response.content.decode()
    assert "404 Error" in content
    assert "The page you are looking for does not exist." in content


@pytest.mark.django_db
@override_settings(DEBUG=False, ALLOWED_HOSTS=['*'])
def test_500_error_handling(monkeypatch, client):
    """ Test that the 500 error view returns a 500 status code and the correct template """
    def fake_index(request):
        raise RuntimeError("Simulated crash")

    # replace the index view with our fake view
    for pattern in urls_module.urlpatterns:
        if getattr(pattern, 'name') == 'index':
            monkeypatch.setattr(pattern, 'callback', fake_index)
            break

    # initialize the client to not raise an exception to the test
    client = Client(raise_request_exception=False)

    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 500
    content = response.content.decode()
    assert "500 Error" in content
    assert "An unexpected error occurred on server" in content
