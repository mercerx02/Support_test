from django.urls import path,include
from . import views
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'', views.UserViewSet)
router2 = routers.SimpleRouter()
router2.register(r'tickets',views.TicketViewSet)

urlpatterns = [
    path('support/',include(router.urls)),
    path('',include(router2.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]