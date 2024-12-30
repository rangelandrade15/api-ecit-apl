from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_X_API_KEY')
        if not api_key:
            return None

        if api_key != 'your-secret-api-key-here':  # Replace with your desired API key
            raise AuthenticationFailed('Invalid API key')

        return (None, None)  # No user object is needed
