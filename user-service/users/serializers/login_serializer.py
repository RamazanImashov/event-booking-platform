from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..validators.login_validator import LoginValidator as LV

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        return LV.user_validator(attrs)
    
    def validate_password(self, attrs):
        return LV.password_validator(self=self, attrs=attrs)
