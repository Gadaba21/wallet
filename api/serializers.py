from rest_framework import serializers

from api.constants import MAX_VALUE_AMOUNT, MIN_VALUE_AMOUNT
from .models import Operation, Wallet


class OperationPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = ['operationType', 'amount']

    def validate_operationType(self, operationType):
        if not operationType:
            raise serializers.ValidationError(
                'Тип операторы не может быть пустым.')
        return operationType

    def validate_amount(self, amount):
        if amount <= MIN_VALUE_AMOUNT:
            raise serializers.ValidationError(
                'Нельзя положить отрицательное количество денег на счет.')
        if amount > MAX_VALUE_AMOUNT:
            raise serializers.ValidationError(
                f'Операции больше {MAX_VALUE_AMOUNT} RPS запрещены.')
        return amount

    def create(self, validated_data):
        if 'amount' not in validated_data:
            raise serializers.ValidationError("Поле 'amount' обязательно.")
        wallet_uuid = self.context['wallet_uuid']
        wallet = Wallet.objects.filter(wallet_uuid=wallet_uuid).first()
        if not wallet:
            raise serializers.ValidationError(
                'Нельзя положить деньги на несуществующий счет.')
        wallet.amount += validated_data['amount']
        wallet.save()
        validated_data['wallet'] = wallet
        return Operation.objects.create(**validated_data)


class WalletGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('amount', 'wallet_uuid')

    def validate(self, id):
        wallet = Wallet.objects.filter(id == id).first()
        if not wallet:
            raise serializers.ValidationError(
                'Нет счета с таким id.')
