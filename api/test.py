from django.test import TestCase
from django.urls import reverse
from .models import Wallet, Operation


class TestOperationCreation(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.wallet = Wallet.objects.create(amount=1000)
        cls.wallet_uuid = cls.wallet.wallet_uuid
        cls.form_data = {
            'operationType': 'DEPOSIT',
            'amount': 200,
        }
        cls.form_data2 = {
            'operationType': 'WITHDRAW',
            'amount': 2000,
        }

    def test_create_operation(self):
        url = reverse('api:wallet-operation',
                      kwargs={'wallet_uuid': self.wallet_uuid}
                      )
        response = self.client.post(url,
                                    data=self.form_data,
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Operation.objects.count(), 1)
        operation = Operation.objects.first()
        self.assertEqual(operation.operationType, 'DEPOSIT')
        self.assertEqual(operation.amount, 200)
        self.assertEqual(operation.wallet, self.wallet)

    def test_not_create_operation(self):
        url = reverse('api:wallet-operation',
                      kwargs={'wallet_uuid': self.wallet_uuid}
                      )
        response = self.client.post(url,
                                    data=self.form_data2,
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Operation.objects.count(), 0)


class TestWalletPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.wallet = Wallet.objects.create(amount=1000)

    def test_wallet_creation(self):
        self.assertEqual(Wallet.objects.count(), 1)
        wallet_from_db = Wallet.objects.first()
        self.assertEqual(wallet_from_db.amount, 1000)
        self.assertIsNotNone(wallet_from_db.wallet_uuid)
