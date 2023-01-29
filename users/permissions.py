from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("admin_login")

        try: #superuser login restriction
            if not request.user.role.name in ["admin", "owner", "renter"]:
                raise
        except:
            return redirect("admin_login")

        return super().dispatch(
            request,
            *args,
            **kwargs,
        )

class AdminRequired(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("admin_login")

        try: #superuser login restriction
            if not request.user.role.name in ["admin"]:
                raise
        except:
            return redirect("admin_login")

        return super().dispatch(
            request,
            *args,
            **kwargs,
        )
