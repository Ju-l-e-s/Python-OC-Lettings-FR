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

Common Tasks
------------

- Search in browser
  - Use your browser's search (Ctrl/Cmd+F) on listing pages to find a specific letting or profile.

- Copy a direct link
  - From a detail page, copy the URL to share a letting or profile with others.

Troubleshooting
---------------

- 404 Not Found
  - Ensure the ID (for lettings) or username (for profiles) exists.

- Permission denied for admin
  - You must be a staff/superuser to access ``/admin/``.

- Empty pages
  - If running locally, make sure you loaded the initial dataset or created objects via admin.

Tips
----

- Use the admin to add/edit lettings and profiles.
- Bookmark frequently viewed lettings or profiles for quick access.
