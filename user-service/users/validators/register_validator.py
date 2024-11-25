from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterValidator:
    @staticmethod
    def validator(attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        if password != password_confirm:
            raise ValidationError(
                """
                ==========================================================
                Password not confirm
                ==========================================================
                """
                )
        return attrs
    
    @staticmethod
    def create(validator_data):
        return User.objects.create_user(**validator_data)
