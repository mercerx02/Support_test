from django.contrib import admin
from .models import Ticket,Message,Categories

admin.site.register(Ticket)
admin.site.register(Message)
admin.site.register(Categories)

