from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import WalletViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('wallets', WalletViewSet, basename='wallet')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
