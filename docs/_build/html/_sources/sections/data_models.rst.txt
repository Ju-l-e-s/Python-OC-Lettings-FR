Database and Models
===================

This section documents the database structure and Django models used by the application.

Model Classes
=============

.. autoclass:: lettings.models.Address
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

.. autoclass:: lettings.models.Letting
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

.. autoclass:: profiles.models.Profile
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

Relationships Overview
----------------------

- ``Letting`` → ``Address`` (One-to-One)
  - Each letting has exactly one address
  - Deleting an address will cascade-delete its associated letting

- ``Profile`` → ``User`` (One-to-One)
  - Each profile is linked to one Django User
  - Access a user's profile via ``user.profile``
  - Deleting a user will cascade-delete their profile


Entity-Relationship Diagram
---------------------------

.. figure:: ../_static/erd.svg
   :alt: ERD
   :align: center
   :figwidth: 80%