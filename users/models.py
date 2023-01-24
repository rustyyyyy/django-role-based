from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import City, District, Municipality, Role, State

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('verified', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email'))

        user = self.model(email=email, password=password, **other_fields)
        user.set_password(password)

        # TODO 1: generating slug
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    mobile = models.CharField(max_length=255, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING,
                             related_name='user_role', null=True)
    slug = models.CharField(max_length=255, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)


class location(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name="location_user", on_delete=models.CASCADE
    )
    municipality = models.ForeignKey(
        Municipality, related_name="location_municipality", on_delete=models.CASCADE
    )
    state = models.ForeignKey(
        State, related_name="location_state", on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District, related_name="location_district", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City, related_name="location_city", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.user.email)
