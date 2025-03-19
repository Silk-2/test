from django.test import TestCase


class test_test_quest(TestCase):

    def test_core_get(self):
        value = self.client.get('api/v1/wallets/123/operation')
        self.assertEqual(value.status_code, 200)

    def test_core_post(self):
        value = self.client.post('api/v1/wallets/123/operation', {'choise_value': 1, 'value': 100})
        self.assertEqual(value.status_code, 200)

    def test_balance_get(self):
        value = self.client.get('api/v1/wallets/123')
        self.assertEqual(value.status_code, 200)
