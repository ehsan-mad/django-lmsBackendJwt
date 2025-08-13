from django.urls import path
from lmsapp.views import RegisterView
from .views import LoginView
urlpatterns = [
    
    path("api/login/", LoginView.as_view(), name="login"),
]
