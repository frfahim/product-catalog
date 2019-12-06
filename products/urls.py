from django.urls import path
from . import views

list_create = {'get': 'list', 'post': 'create'}
details_update = {'get': 'retrieve', 'put': 'update'}

urlpatterns = [
    path(
        'products/',
        views.ProductListViewSet.as_view(list_create),
        name='product-list'
    ),
    path(
        'products/<slug>/',
        views.ProductListViewSet.as_view(details_update),
        name='product-details'
    ),
    path(
        'products/<slug>/attributes/',
        views.ProductAttributeViewSet.as_view(list_create),
        name='product-attribute'
    ),
    path(
        'products/<slug>/prices/',
        views.ProductPriceViewSet.as_view(list_create),
        name='product-price'
    ),
]