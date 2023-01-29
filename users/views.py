from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .permissions import LoginRequiredMixin, AdminRequired
from .forms import OwnerCreationForm
# Create your views here.


class Login(View):
    def get(self, request):
        logout(request)
        return render(request, "auth/login.html")

    def post(self, request):
        try:
            user = authenticate(
                username=request.POST["email"], password=request.POST["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            raise
        except:
            return redirect("admin_login")


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        
        if user.role.name == "admin":
            return render(request, "admin/index.html")

        return render(request, "home/index.html")


class OwnerView(AdminRequired, View):
    def get(self, request):
        form = OwnerCreationForm()
        return render(request, "admin/add_owner.html", {"form": form})