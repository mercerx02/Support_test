from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Ticket
from .tasks import send_email


@receiver(post_save,sender=Ticket)
def post_save_ticket(instance,created:bool,**kwargs) -> None:
    '''
    Django-Signal which runs celery-task.
    '''
    email = instance.owner.email
    category = str(instance.category)
    send_email.delay(email,category,created)



