
from django.urls import path,include
from . import views
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router2 = routers.SimpleRouter()
router2.register(r'tickets',views.TicketViewSet)

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('support/',include(router.urls)),
    path('',include(router2.urls)),
    path('support/tickets/', views.AllTicketList.as_view()),
    path('tickets/message/',views.MessagesList.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns = [
#     path('auth/', include('rest_framework.urls')),
#     path('support/',include(router.urls)),
#     path('support/tickets/', views.AllTicketList.as_view()),
#     path('tickets/',views.TicketViewSet.as_view({'get':'list'})),
#     path('tickets/create/',views.TicketViewSet.as_view({'post':'create'})),
#     path('tickets/message/',views.MessagesList.as_view())
#
# ]
