from django.urls import path
from accounts.views import UserSignupView

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="signup"),
]
