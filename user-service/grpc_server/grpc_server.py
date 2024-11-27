from pathlib import Path
import os
import sys
import grpc
import django
from concurrent import futures
import user_pb2
import user_pb2_grpc

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.setting.settings')
django.setup()

from django.contrib.auth import get_user_model
from profiles.models import OrganizerProfile
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.exceptions import AuthenticationFailed

CustomUser = get_user_model()


def authenticate_token(token: str):
    jwt_authenticator = JWTAuthentication()
    try:
        validated_token = jwt_authenticator.get_validated_token(token)
        user = jwt_authenticator.get_user(validated_token)
        print(f"Authenticated user: {user}, ID: {user.id}")
        return user  # Authenticated user object
    except AuthenticationFailed:
        print("Token authentication failed")
        return None


class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        try:
            user = CustomUser.objects.get(id=request.id)
            return user_pb2.UserResponse(
                id=str(user.id),
                username=user.username,
                email=user.email,
                role=user.role
            )
        except CustomUser.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.UserResponse()

    def CheckVerifyToken(self, request, context):
        user = authenticate_token(request.token)
        print("==========================================================")
        print(f"User object: {user}")
        if user:
            print(f"User ID: {user.id}, Role: {user.role}")
            return user_pb2.TokenVerifyResponse(
                is_valid=True,
                user_id=str(user.id),
                role=user.role
            )
        print("Invalid token")
        context.set_code(grpc.StatusCode.UNAUTHENTICATED)
        context.set_details('Invalid token')
        return user_pb2.TokenVerifyResponse(is_valid=False)

    def GetOrganizerProfile(self, request, context):
        try:
            profile = OrganizerProfile.objects.get(user_id=request.id)
            return user_pb2.OrgProfileResponse(
                id=str(profile.user.id),
                organization_name=profile.organization_name,
                organization_email=profile.organization_email,
                is_verified=profile.is_verified,
                role=profile.user.role
            )
        except OrganizerProfile.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Organizer profile not found')
            return user_pb2.OrgProfileResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
