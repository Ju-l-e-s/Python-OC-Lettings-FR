from django.http import HttpRequest, HttpResponse
import sentry_sdk


class SentryExceptionMiddleware:
    """
    Middleware that captures all exceptions (including HTTP 404 and PermissionDenied)
    and forwards them to Sentry for centralized error tracking.
    """

    def __init__(self, get_response) -> None:
        """Initialize the middleware."""
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Call the middleware."""
        response = self.get_response(request)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception) -> None:
        """Process the exception."""
        sentry_sdk.capture_exception(exception)
        return None
