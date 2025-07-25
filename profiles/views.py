"""Views for the profiles application.

This module defines the views used in the profiles application,
including index and profile views.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
import logging

from .models import Profile

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the list of profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    profiles_list = Profile.objects.all()
    logger.info(
        "Displaying profiles list",
        extra={"count": profiles_list.count()}
    )
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Display a profile.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    profile = get_object_or_404(Profile, user__username=username)
    logger.info(
        "Displaying profile detail",
        extra={"username": username}
    )
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
