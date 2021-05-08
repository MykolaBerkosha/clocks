
from django.urls import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

from slugify import slugify_url


class Product(models.Model):

    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('Category'),
        related_name='products',
        on_delete=models.CASCADE
    )

    name = models.CharField(_('Name'), max_length=255)

    price = models.FloatField(_('Price'))

    logo = models.ImageField(_('Logo'), upload_to='product_logos')

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
