from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    Product,
    ProductAttribute,
    ProductPrice,
)
from .serializers import (
    ProductSerializer,
    ProductAttributeSerializer,
    ProductPriceSerializer,
)

class ProductListViewSet(viewsets.ModelViewSet):
    """
    get:
    Return a list of products
    post:
    Create a product with product name and code (slug will be auto generate)
    put:
    Update a product data
    get details:
    Return details of a product
    """

    permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    queryset = Product.objects.filter(is_available=True).order_by('-id')


class ProductAttributeViewSet(viewsets.ModelViewSet):
    """
    get:
    Return list of product attributes
    post:
    Create a product attribute with color and size
    """
    # permission_classes = (IsAuthenticated, )
    serializer_class = ProductAttributeSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return ProductAttribute.objects.filter(
            product__slug=self.kwargs.get('slug')
        ).order_by('-id')

    def create(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(slug=self.kwargs.get('slug'))
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductPriceViewSet(viewsets.ModelViewSet):
    """
    get:
    Return list of product price
    post:
    Create a product attribute with price and date
    """
    # permission_classes = (IsAuthenticated, )
    serializer_class = ProductPriceSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return ProductPrice.objects.filter(
            product__slug=self.kwargs.get('slug')
        ).order_by('-id')

    def create(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(slug=self.kwargs.get('slug'))
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
