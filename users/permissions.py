from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("admin_login")

        if not request.user.role.name in ["admin", "owner", "renter"]:
            return redirect("admin_login")
        return super().dispatch(
            request,
            *args,
            **kwargs,
        )
