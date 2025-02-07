from django.contrib import admin

from .models import Operation, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    """Класс настройки раздела кошельков."""

    list_display = ('id', 'amount')
    search_fields = ('id',)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    """Класс настройки раздела операций."""

    list_display = ('id', 'wallet', 'amount', 'operationType')
