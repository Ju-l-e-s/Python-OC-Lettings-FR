Deployment and CI/CD
====================

Overview
--------

This project uses an automated CI/CD pipeline with GitHub Actions, triggered on every push to the ``main`` branch.
The pipeline has two main stages:

1. **Tests and validation**: Run unit tests, linting, and ensure code coverage (>= 80%).
2. **Deployment**: Build the Docker image, push to Docker Hub, and deploy to Render.

Required Configuration
----------------------

- A `Docker Hub <https://hub.docker.com/>`_ account to host images
- A `Render <https://render.com/>`_ account for hosting
- The following secrets must be set in your GitHub repository settings:

  - ``DOCKERHUB_USERNAME``: Your Docker Hub username
  - ``DOCKERHUB_TOKEN``: Your Docker Hub access token
  - ``RENDER_DEPLOY_HOOK_URL``: The Render deployment webhook URL

Render Environment Variables
----------------------------

In the Render dashboard, configure the following environment variables:

- ``ALLOWED_HOSTS``: ``oc-lettings-latest-qgxn.onrender.com, oc-lettings.onrender.com``
- ``DEBUG``: ``False``
- ``SECRET_KEY``: Your Django secret key
- ``SENTRY_DSN``: Your Sentry DSN for error monitoring

Deployment Steps
----------------

1. Configure the secrets in GitHub repository settings.
2. Configure the environment variables in the Render dashboard.
3. Push changes to the ``main`` branch to trigger the pipeline.

CI/CD Workflow
--------------

The pipeline is defined in ``.github/workflows/ci-cd.yml`` and includes:

1. **Tests and validation** (on every push and pull request):

   - Install dependencies
   - Check code style with ``flake8``
   - Run unit tests with a minimum coverage of 80%

2. **Publish Docker image** (only on ``main``):

   - Build the Docker image
   - Push to Docker Hub with tags:

     - ``latest`` for the latest stable version
     - ``[commit-hash]`` for traceability

3. **Deploy to Render** (only on ``main``):

   - Trigger via webhook
   - Automatic service restart
   - Application available at: https://oc-lettings-latest-qgxn.onrender.com
