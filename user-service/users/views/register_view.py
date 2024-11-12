from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from services.register_service import V1RegisterService as v1_rsr
from serializers.user_serializer import RegisterSerializer as rs
from drf_spectacular.utils import extend_schema


@extend_schema(tags=("Register"))
class V1RegisterView(APIView):
    service = v1_rsr()
    permission_classes = (AllowAny,)
    
    
    @extend_schema(
        description="",
        request=rs,
        responses={201: rs}
    )
    def post(self, request):
        data = request.data
        status_code = self.service.register_email(data=data)
        return Response({"data": "Good, Register successful for email",
                         "status": status_code}, status=HTTP_201_CREATED)


