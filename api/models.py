import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.constants import MAX_LENGTH_TYPE, MAX_VALUE_AMOUNT, MIN_VALUE_AMOUNT


class Operation(models.Model):

    operationType = models.CharField(max_length=MAX_LENGTH_TYPE,
                                     verbose_name='Операция')
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(
                MIN_VALUE_AMOUNT,
                message=f'Количество не может быть меньше {MIN_VALUE_AMOUNT}'
            ),
            MaxValueValidator(
                MAX_VALUE_AMOUNT,
                message=f'Количество не может быть больше {MAX_VALUE_AMOUNT}'
            )
        ],)
    wallet = models.ForeignKey('Wallet',
                               on_delete=models.CASCADE,
                               verbose_name='Кошелек')

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'


class Wallet(models.Model):
    amount = models.PositiveIntegerField(verbose_name='Количество средств')
    wallet_uuid = models.UUIDField(default=uuid.uuid4,
                                   editable=False,
                                   unique=True)

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return f"Wallet {self.wallet_uuid}"
