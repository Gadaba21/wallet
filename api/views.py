from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from api.models import Wallet
from api.serializers import OperationPostSerializer, WalletGetSerializer


class WalletViewSet(viewsets.ModelViewSet):
    """Получение текущего состояния кошелька пользователя."""

    queryset = Wallet.objects.all()
    serializer_class = WalletGetSerializer
    lookup_field = 'wallet_uuid'

    @action(detail=True,
            methods=['post'],
            url_path='operation',
            url_name='operation'
            )
    def operation(self, request, wallet_uuid=None):
        serializer = OperationPostSerializer(
            data=request.data,
            context={'wallet_uuid': wallet_uuid}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
