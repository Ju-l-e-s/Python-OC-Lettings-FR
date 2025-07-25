"""Views for the lettings application.

This module defines the views used in the lettings application,
including index and letting views.
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
import logging

from lettings.models import Letting

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the list of lettings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    lettings_list = Letting.objects.all()
    logger.info(
        "Displaying lettings list",
        extra={"count": lettings_list.count()}
    )
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request: HttpRequest, letting_id) -> HttpResponse:
    """
    Display a letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    logger.info(
        "Displaying letting detail",
        extra={"letting_id": letting.id, "title": letting.title}
    )
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
