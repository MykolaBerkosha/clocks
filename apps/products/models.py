
from django.urls import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

from slugify import slugify_url

from availability.models import AvailabilityField


class Product(models.Model):

    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('Category'),
        related_name='products',
        on_delete=models.CASCADE
    )

    name = models.CharField(_('Name'), max_length=255, db_index=True)

    price = models.FloatField(_('Price'))

    logo = models.ImageField(_('Logo'), upload_to='product_logos')

    tags = models.TextField(
        _('Tags'),
        max_length=1000,
        db_index=True,
        blank=True)

    availability = AvailabilityField()

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return slugify_url(self.name)

    def get_absolute_url(self):
        return reverse_lazy('products:detail', args=[
            self.category.slug, self.category.id, self.slug, self.id
        ])

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
