import factory
from django.contrib.auth.models import User

from products.models import (
    Product,
    ProductAttribute,
    ProductPrice,
)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    email = factory.LazyAttribute(lambda user: '{}@mail.com'.format(user.first_name))
    password = factory.PostGenerationMethodCall('set_password', 'testpass')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('text')
    code = factory.Faker('ssn')


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttribute

    color = factory.Faker('color_name')


class ProductPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductPrice

    price = factory.Faker('random_number')
