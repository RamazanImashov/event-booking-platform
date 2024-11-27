
import os
import sys
from decouple import config as deconf

sys.path.append(os.path.abspath(deconf("ABS_PASH")))

import grpc
from . import user_pb2
from . import user_pb2_grpc

GRPC_SERVER = deconf("GRPC_SERVER")

channel = grpc.insecure_channel(f'{GRPC_SERVER}:50051')
stub = user_pb2_grpc.UserServiceStub(channel)


def get_user(user_id: str):
    try:
        response = stub.GetUser(user_pb2.UserRequest(id=user_id))
        return response
    except grpc.RpcError as e:
        print(f"gRPC error: {e}")
        return None


def verify_token(token: str):
    try:
        response = stub.CheckVerifyToken(user_pb2.TokenVerifyRequest(token=token))
        print(f"Verify token response: {response}")
        if response.is_valid:
            return response
        else:
            print("Token is not valid")
            return None
    except grpc.RpcError as e:
        print(f"gRPC error during token verification: {e}")
        return None


def get_organizer_profile(user_id: str):
    try:
        response = stub.GetOrganizerProfile(user_pb2.OrgProfileRequest(id=user_id))
        if response.role != "organizer":
            raise Exception("User not organizer")
        return response
    except grpc.RpcError as e:
        print(f"gRPC error: {e}")
        return None

