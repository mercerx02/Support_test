
from django.urls import path,include
from . import views
urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('support/users/', views.UserList.as_view()),
    path('support/users/<int:pk>/', views.UserDetail.as_view()),
    path('support/tickets/', views.AllTicketList.as_view()),
    path('tickets/',views.UsersTicketAPIView.as_view()),
    path('tickets/create/',views.CreateTicketVIEW.as_view()),
    path('tickets/message/',views.MessagesList.as_view())

]

