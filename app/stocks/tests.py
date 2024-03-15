import json
from django.test import TestCase


class BuyStockViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view_path = '/buystock/'
        cls.message_deny = 'Deny'
        cls.message_accept = 'Accept'

    def test_url_exists(self):
        response = self.client.post(self.view_path)
        self.assertEqual(response.status_code, 200)

    def test_url_response_404_when_user_not_exist(self):
        body = {'user': 'user3', 'stock': 'stock1', 'quantity': 10}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(content['message'], self.message_deny)

    def test_url_response_400_when_credit_is_not_sufficient(self):
        body = {'user': 'user1', 'stock': 'stock1', 'quantity': 10000000000}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['message'], self.message_deny)

    def test_url_response_400_when_quantity_is_not_positive(self):
        body = {'user': 'user1', 'stock': 'stock1', 'quantity': -1}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['message'], self.message_deny)

    def test_url_response_400_when_user_not_in_request_body(self):
        body = {'stock': 'stock1', 'quantity': 10}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['message'], self.message_deny)

    def test_url_response_400_when_stock_not_in_request_body(self):
        body = {'user': 'user1', 'quantity': 10}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['message'], self.message_deny)

    def test_url_response_400_when_quantity_not_in_request_body(self):
        body = {'user': 'user3', 'stock': 'stock1'}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['message'], self.message_deny)

    def test_url_succeed(self):
        body = {'user': 'user1', 'stock': 'stock1', 'quantity': 10}
        response = self.client.post(self.view_path,
                                    json.dumps(body),
                                    content_type='application/json')
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['message'], self.message_accept)
