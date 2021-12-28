
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):

    first_name = models.CharField(
        _('First name'), max_length=255, blank=True)

    last_name = models.CharField(
        _('Last name'), max_length=255, blank=True)

    mobile = models.CharField(_('Mobile number'), max_length=255)

    created = models.DateTimeField(_('Created'), auto_now_add=True)

    DELIVERY_METHOD_CHOISE = (
        ("NOVA-POSHTA", "Nova-poshta"),
        ("UKR-POSHTA", "Ukr-poshta"),
        ("Delivery-POSHTA", "Delivery-poshta"),
        ("SELF-PICKUP", "Self-pickup")
    )

    delivery_method = models.CharField(max_length=22, choices=DELIVERY_METHOD_CHOISE, default= "SELF-PICKUP")

    delivery_district_address = models.CharField(_('Delivery district address'), max_length=255, blank=True)

    delivery_region_address = models.CharField(_('Delivery district address'), max_length=255, blank=True)

    post_office = models.CharField(_('Post office'), max_length=255, blank=True)

    def __str__(self):
        return 'Order #{} for {}'.format(self.id or '?', self.first_name)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderedProduct(models.Model):

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')

    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)

    price = models.FloatField()

    def __str__(self):
        return '{} {}'.format(self.product.name, self.product.price)
