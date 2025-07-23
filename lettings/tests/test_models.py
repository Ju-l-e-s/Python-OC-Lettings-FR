from django.db import IntegrityError
import pytest

from lettings.models import Address, Letting


@pytest.fixture
def valid_address_data():
    """Fixture providing valid address data."""
    return {
        'number': 742,
        'street': 'Evergreen Terrace',
        'city': 'Springfield',
        'state': 'IL',
        'zip_code': 12345,
        'country_iso_code': 'USA'
    }


@pytest.fixture
def test_address(valid_address_data):
    """Fixture providing a saved Address instance."""
    return Address.objects.create(**valid_address_data)


# -----------------------------
# Address Model Tests
# -----------------------------

@pytest.mark.django_db
def test_str_address(valid_address_data):
    """__str__ must return '<number> <street>'."""
    address = Address.objects.create(**valid_address_data)
    expected = f"{valid_address_data['number']} {valid_address_data['street']}"
    assert str(address) == expected


# -----------------------------
# Letting Model Tests
# -----------------------------

@pytest.mark.django_db
def test_str_letting(test_address):
    """__str__ must return the title of the letting."""
    letting = Letting.objects.create(title="My Home", address=test_address)
    assert str(letting) == "My Home"


@pytest.mark.django_db
def test_one_to_one_uniqueness(test_address):
    """
    An Address cannot be linked to two Letting instances.
    Should raise IntegrityError.
    """
    Letting.objects.create(title="First", address=test_address)
    with pytest.raises(IntegrityError):
        Letting.objects.create(title="Second", address=test_address)


@pytest.mark.django_db
def test_address_cascade_delete(test_address):
    """
    Deleting an Address should delete the associated Letting (CASCADE).
    """
    letting = Letting.objects.create(title="Cascade Test", address=test_address)
    test_address.delete()
    assert not Letting.objects.filter(id=letting.id).exists()


@pytest.mark.django_db
def test_delete_letting_keeps_address(test_address):
    """
    Deleting a Letting should not delete the Address.
    """
    letting = Letting.objects.create(title="Keep Address", address=test_address)
    letting.delete()
    assert Address.objects.filter(id=test_address.id).exists()
