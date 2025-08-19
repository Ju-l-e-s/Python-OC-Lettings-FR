Installation
============

Local Development
-----------------

**Prerequisites**

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher


macOS / Linux
~~~~~~~~~~~~~

**Clone the repository**

.. code-block:: bash

   cd /path/to/put/project/in
   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

**Create the virtual environment**

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   python -m venv venv
   # On Ubuntu, if you get "package not found", run:
   apt-get install python3-venv
   source venv/bin/activate

Confirm that:

- ``which python`` points to the virtualenv Python
- ``python --version`` is 3.6 or higher
- ``which pip`` points to the virtualenv pip

Deactivate the environment with:

.. code-block:: bash

   deactivate

**Initialize environment variables**

At the project root, create a `.env` file and add:

.. code-block:: bash

   DEBUG=False
   SECRET_KEY=your_secret_key
   SENTRY_DSN=https://<publicKey>@o0.ingest.sentry.io/<projectID>

**Run the site locally**

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pip install --requirement requirements.txt
   python manage.py runserver

Then open http://localhost:8000 in a browser. You should see several profiles and lettings.

**Linting**

.. code-block:: bash

   source venv/bin/activate
   flake8

**Unit tests**

.. code-block:: bash

   source venv/bin/activate
   pytest

**Database**

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   sqlite3
   .open oc-lettings-site.sqlite3
   .tables
   pragma table_info(Python-OC-Lettings-FR_profile);
   select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
   .quit

**Admin panel**

Go to http://localhost:8000/admin and log in with:

- Username: ``admin``
- Password: ``Abc1234!``

Windows
~~~~~~~

Same steps as above, but using PowerShell:

- Activate virtualenv:

.. code-block:: powershell

   .\venv\Scripts\Activate.ps1

- Replace ``which <command>`` with:

.. code-block:: powershell

   (Get-Command <command>).Path
