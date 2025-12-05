# middleware.py
from django.http import HttpResponsePermanentRedirect

class RedirectApexToWWW:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == "harrisonogdencarr.com":
            return HttpResponsePermanentRedirect(
                "https://www.harrisonogdencarr.com" + request.get_full_path()
            )
        return self.get_response(request)