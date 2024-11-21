from ..serializers.login_serializer import LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class LoginViewEmail(ObtainAuthToken):
    serializer_class = LoginSerializer
