from django.urls import path, include
from views.register_view import V1RegisterView

urlpatterns = [
    path("v1_register/", V1RegisterView.as_view())
]