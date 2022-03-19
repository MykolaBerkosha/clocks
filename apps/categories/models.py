
from django.urls import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

from slugify import slugify_url


class Category(models.Model):

    name = models.CharField(_('Name'), max_length=255)

    logo = models.ImageField(
        _('Logo'), upload_to='category_logos', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def slug(self):
        return slugify_url(self.name)

    def get_absolute_url(self):
        return reverse_lazy('products:list', args=[self.slug, self.id])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
