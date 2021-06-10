
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Review(models.Model):

    name = models.CharField(_("Name"), max_length=255)

    text = models.TextField(_('Text'), max_length=1000)

    rating = models.IntegerField(
        _('Rating'),
        choices=((i, i) for i in range(1, 6))
    )
