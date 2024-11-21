from users.serializers.register_serializer import RegisterSerializer as rs
from rest_framework.status import HTTP_201_CREATED


class V1RegisterService:
    @staticmethod
    def register_email(data):
        serializer = rs(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HTTP_201_CREATED