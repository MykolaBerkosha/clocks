
from django import template

from apps.cart.lib import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def get_cart(context):
    return Cart(context.request.session)
