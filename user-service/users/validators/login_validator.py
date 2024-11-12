from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class LoginValidator:
    @classmethod
    def user_validator(attrs):
        username = attrs.get("username")
        if not User.objects.filter(username=username).first():
            raise ValidationError(
                """
                ==========================================================
                User not found
                ==========================================================
                """
                )
        return attrs
    
    @staticmethod
    def password_validator(self, attrs):
        request = self.context.get("request")
        username = attrs.get("email")
        password = attrs.get("password")
        
        if username and password:
            user = authenticate(username=username, password=password, request=request)
            
            if not user:
                raise ValidationError(
                """
                ==========================================================
                Incorrect username or password
                ==========================================================
                """
                )
        else:
            raise ValidationError(
                """
                ==========================================================
                Username and password necessarily
                ==========================================================
                """
                )
        attrs["user"] = user
        return attrs
    