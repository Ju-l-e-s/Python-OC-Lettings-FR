User Guide
==========

This guide explains how to use the OC Lettings application through typical user journeys.

Navigation
----------

- Home page: ``/`` — Entry point with links to Lettings and Profiles.
- Admin: ``/admin/`` — Django admin interface for staff users.

Lettings
--------

- List lettings: ``/lettings/``
  - Shows all available lettings.
  - Click a letting to view its details.

- View a letting: ``/lettings/<id>/``
  - Example: ``/lettings/1/``
  - Displays title, address and detailed information.

Profiles
--------

- List profiles: ``/profiles/``
  - Shows all user profiles with links to detail pages.

- View a profile: ``/profiles/<username>/``
  - Example: ``/profiles/john/``
  - Displays username and favorite city.
