from django.contrib import admin
from .models import Role, OwnerType, PropertyType, Municipality, State, District, City


# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = ["id", "name"]


@admin.register(OwnerType)
class OwnerTypeAdmin(admin.ModelAdmin):
    model = OwnerType
    list_display = ["id", "name"]


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    model = PropertyType
    list_display = ["id", "name"]


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    model = Municipality
    list_display = ["id", "name"]

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ["id", "name"]

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = ["id", "name", "state"]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ["id", "name", "district"]


