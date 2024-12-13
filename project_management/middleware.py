from django.utils.deprecation import MiddlewareMixin

class CorrectMimeTypeMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.endswith('.css'):
            response['Content-Type'] = 'text/css'
        return response