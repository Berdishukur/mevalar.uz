import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Order,OrderProduct


@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:  # Check if a new record is created
        token = settings.TELEGRAM_BOT_TOKEN
        method = 'sendMessage'
        message_text = f"Client: {instance.customer} \n Address: {instance.address} \n " \
                       f"Buyurtma qilingan vaqt: {instance.created_at}\n tel:{instance.customer.phone_number} "

        response = requests.post(
            url=f'https://api.telegram.org/bot{token}/{method}',
            data={'chat_id': 5259578459, 'text': message_text}
        ).json()
