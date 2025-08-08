"""Data models for the lettings application.

This module defines the database models used in the lettings application,
including Address and Letting models.
"""
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Represents a physical address for a property.

    Attributes:
        number (int): The street number. Must be a positive integer ≤ 9999.
        street (str): The street name. Maximum length of 64 characters.
        city (str): The city name. Maximum length of 64 characters.
        state (str): The state code. Exactly 2 characters.
        zip_code (int): The postal code. Must be a 5-digit number.
        country_iso_code (str): The ISO country code. Exactly 3 characters.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        db_table = 'oc_lettings_site_address'

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Represents a property available for rent.

    Attributes:
        title (str): The title f the property. Maximum 256 characters.
        address (Address): A one-to-one relationship with the Address model.
        Deleted if the address is deleted.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = 'oc_lettings_site_letting'

    def __str__(self):
        return self.title
