from rest_framework import serializers
from django.contrib.auth import get_user_model
from validators.register_validator import RegisterValidator as RV
from validators.login_validator import LoginValidator as LV

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "role", "password", "password_confirm")
        
    def validate(self, attrs):
        return RV.validator(attrs=attrs)
    
    def create(self, validated_data):
        return RV.create(validated_data=validated_data)
    
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
    def validate(self, attrs):
        return LV.user_validator(attrs)
    
    def validate_password(self, attrs):
        return LV.password_validator(self=self, attrs=attrs)