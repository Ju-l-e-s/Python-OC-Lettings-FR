"""Views for the oc_lettings_site application.

This module defines the views used in the oc_lettings_site application,
including index view.
"""
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, 'index.html')
