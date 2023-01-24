from django.contrib import admin
from .models import Property
# Register your models here.


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    model = Property
    list_display = ["id", "user"]
