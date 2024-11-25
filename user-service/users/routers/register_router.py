from django.urls import path, include
from users.views.register_view import V1RegisterView

urlpatterns = [
    path("register/", V1RegisterView.as_view())
]
