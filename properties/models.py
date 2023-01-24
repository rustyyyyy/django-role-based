from django.db import models
from users.models import CustomUser, State, District, City


# Create your models here.
class Property(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name="property_user", on_delete=models.CASCADE
    )
    state = models.ForeignKey(
        State, related_name="property_state", on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District, related_name="property_district", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City, related_name="property_city", on_delete=models.CASCADE
    )
    is_booked = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property'

    def __str__(self):
        return str(self.user.email)
 