from support.celery import app
from support import settings
from django.core.mail import send_mail

@app.task()
def send_email(email:str,category:str,created:bool) -> None:
    """
    A function that receives an email, a modified category, and a boolean as input.
    Sends a message to the user's email about changing or creating a ticket.
"""
    if created:
        try:
            send_mail(
                'Support Service',

            'You have submitted a Ticket to the Support service. Our staff will review your Ticket shortly. '
            'Thanks for using our service.',

           settings.EMAIL_HOST_USER,

           [f'{str(email)}']

        )
        except:
            pass

    else:
        try:
            send_mail(
                'Support Service',

                f'Your Ticket status has changed to {category}'
                'Thanks for using our service.',

                settings.EMAIL_HOST_USER,

                [f'{email}']

        )
        except:
            pass