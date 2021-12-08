
from django.db import models
from apps.products.constants import AVAILABILITY_IN_STOCK


class AvailabilityQuerySet(models.QuerySet):

    def default(self):
        return self.filter(is_default=True).first()
