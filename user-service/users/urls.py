from django.urls import path, include

urlpatterns = [
    path("v1/", include("users.routers.register_router")),
    path("v1/", include("users.routers.login_router")),
]
