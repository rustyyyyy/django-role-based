from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, location

admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','id',  'role', 'verified', 'verified_at']
    fieldsets = (
        (None, {"fields": (
            "email", "password", "is_superuser", "verified", "role"
        )}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    ordering = ("id",)
    search_fields = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(location)
class locationAdmin(admin.ModelAdmin):
    model = location
    list_display = ["id", "user", "municipality", "state", "district", "city"]
