from django.utils.cache import add_never_cache_headers

class DisableClientSideCachingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        add_never_cache_headers(response)
        response['Pragma'] = 'no-cache'
        # Code to be executed for each request/response after
        # the view is called.

        return response