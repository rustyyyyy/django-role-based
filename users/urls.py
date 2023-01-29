from django.urls import path

from .views import Dashboard, Login, OwnerView

urlpatterns = [
    path("login/", Login.as_view(), name="admin_login"),
    path("", Dashboard.as_view(), name="dashboard"),
    path("owner", OwnerView.as_view(), name="owner"),
]