from rest_framework import serializers
from .models import Product, ProductAttribute, ProductPrice


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = [
			'id',
			'name',
			'slug',
			'code',
		]

		read_only_fields = ('id', 'slug')


class ProductAttributeSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductAttribute
		fields = [
			'id',
			'color',
			'size',
		]

		read_only_fields = ('id',)


class ProductPriceSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductPrice
		fields = [
			'id',
			'price',
			'date',
		]

		read_only_fields = ('id',)
