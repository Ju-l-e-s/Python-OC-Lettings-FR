API / Views / URLs
==================

Lists all available URL routes in the OC Lettings application and their purpose.

Main Project URLs
-----------------

.. literalinclude:: ../../oc_lettings_site/urls.py
   :language: python
   :start-after: urlpatterns = [
   :end-before: ]
   :dedent: 4
   :linenos:

Lettings Application
--------------------

.. literalinclude:: ../../lettings/urls.py
   :language: python
   :start-after: urlpatterns = [
   :end-before: ]
   :dedent: 4
   :linenos:

Profiles Application
--------------------

.. literalinclude:: ../../profiles/urls.py
   :language: python
   :start-after: urlpatterns = [
   :end-before: ]
   :dedent: 4
   :linenos:

Available Endpoints
-------------------

Main Pages
~~~~~~~~~~
- ``/`` - Home page
- ``/admin/`` - Django admin interface

Lettings
~~~~~~~~
- ``/lettings/`` - List all available lettings
- ``/lettings/<id>/`` - Show specific letting details

Profiles
~~~~~~~~
- ``/profiles/`` - List all user profiles
- ``/profiles/<username>/`` - Show specific user profile details
