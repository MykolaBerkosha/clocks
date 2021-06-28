
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):

    first_name = models.CharField(_('First name'), max_length=255)

    last_name = models.CharField(_('Last name'), max_length=255)

    mobile = models.CharField(_('Mobile number'), max_length=255)

    def __str__(self):
        return 'Order #{} for {}'.format(self.id or '?', self.first_name)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
