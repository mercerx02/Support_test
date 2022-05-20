
from django.urls import path
from . import views


urlpatterns = [

    path('support/tickets/', views.AllTicketList.as_view()),
    path('tickets/message/',views.MessagesList.as_view()),
]

