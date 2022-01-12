from django.db import models


class ProductManager(models.Manager):
    def visible(self):
        return self.filter(is_visible = 'visible')
