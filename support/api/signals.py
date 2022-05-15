from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Ticket
from support import settings
from django.core.mail import send_mail

@receiver(post_save,sender=Ticket)
def post_save_ticket(instance,created,**kwargs):
    ''' Джанго-Сигнал, который отправляет сообщение Юзеру на его почту при создании Тикета.
    Так же отправляет уведомление об измении статуса тикета.
    '''

    if created:
        try:
            send_mail(
                'Support Service',

            'You have submitted a Ticket to the Support service. Our staff will review your Ticket shortly. '
            'Thanks for using our service.',

           settings.EMAIL_HOST_USER,

           [f'{str(instance.owner.email)}']

        )
        except:
            pass

    else:
        try:
            send_mail(
                'Support Service',

                f'Your Ticket status has changed to {instance.owner.category}'
                'Thanks for using our service.',

                settings.EMAIL_HOST_USER,

                [f'{str(instance.owner.email)}']

        )
        except:
            pass

