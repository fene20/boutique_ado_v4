from django.db.models.signals import post_save, post_delete  # post so these signals are sent by django to the whole application after a model instance is saved or deleted.
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    #  print('delete signal received!')
    instance.order.update_total()
