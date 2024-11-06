# myapp/signals.py
'''from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Invoice

@receiver(post_save, sender=Order)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        # Creating an invoice with an invalid amount to trigger an error
        Invoice.objects.create(order=instance, amount="invalid_amount")
'''

# myapp/signals.py
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Invoice

@receiver(post_save, sender=Order)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        # Creating an invoice with an invalid amount to trigger an error
        Invoice.objects.create(order=instance, amount="invalid_amount")

