import json
from django.urls import reverse
from faker import Faker

from .test_case import CommonTestCase
from . import (
    UserFactory,
    ProductFactory,
)


class ProductListAPITest(CommonTestCase):
    url = reverse('product-list')
    fake = Faker()

    def test_product_list_get(self):
        user = UserFactory()
        ProductFactory.create_batch(10)

        # get product list without login
        request = self.client.get(self.url)
        self.assertUnauthorized(request)

        login = self.client.login(username=user.username, password="testpass")
        self.assertTrue(login)

        # get product list with login
        request = self.client.get(self.url)
        self.assertSuccess(request)

        # check request data total with total created product
        self.assertEqual(request.data['count'], 10)

        # logout
        self.client.logout()

    def test_product_post(self):
        user = UserFactory()
        data = {
            'name': self.fake.first_name(),
            'code': self.fake.ssn()
        }

        # post product api without login
        request = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertUnauthorized(request)

        login = self.client.login(username=user.username, password="testpass")
        self.assertTrue(login)

        # post product api with login
        request = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertCreated(request)

        # match data
        self.assertEqual(request.data['name'], data['name'])
        self.assertEqual(request.data['code'], data['code'])

        # logout
        self.client.logout()

    def test_product_details(self):
        user = UserFactory()
        product = ProductFactory()
        self.url = reverse('product-details', args=[product.slug])

        # get product details without login
        request = self.client.get(self.url)
        self.assertUnauthorized(request)

        login = self.client.login(username=user.username, password="testpass")
        self.assertTrue(login)

        # get product details with login
        request = self.client.get(self.url)
        self.assertSuccess(request)

        # compare request data
        self.assertEqual(request.data['name'], product.name)
        self.assertEqual(request.data['code'], product.code)

        # logout
        self.client.logout()

    def test_product_put(self):
        user = UserFactory()
        product = ProductFactory()
        self.url = reverse('product-details', args=[product.slug])
        data = {
            'name': self.fake.first_name()
        }

        # update product without login
        request = self.client.put(self.url, data)
        self.assertUnauthorized(request)

        login = self.client.login(username=user.username, password="testpass")
        self.assertTrue(login)

        # update product with login
        request = self.client.put(self.url, data)
        self.assertSuccess(request)

        # compare request data
        self.assertEqual(request.data['name'], data['name'])

        # logout
        self.client.logout()
