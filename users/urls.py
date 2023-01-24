from django.urls import path

from .views import Dashboard, Login

urlpatterns = [
    path("login/", Login.as_view(), name="admin_login"),
    path("", Dashboard.as_view(), name="dashboard"),
]