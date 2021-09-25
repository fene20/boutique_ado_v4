from django import template


register = template.Library()

@register.filter(name='calc_subtotal') # in django documentation - creating custom template tags and filters.
def calc_subtotal(price, quantity):
    return price * quantity