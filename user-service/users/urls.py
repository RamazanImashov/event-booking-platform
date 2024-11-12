from django.urls import path, include
import routers.register_router as v1_reg_r

urlpatterns = [
    path("v1/", include(v1_reg_r)),
]