from datetime import datetime, date

from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    slug = models.SlugField(unique=True)
    code = models.CharField(blank=True, null=True, max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


    def save(self, *args, **kwargs):
        if not self.id:
            now = datetime.now()
            slug = f"{self.name}-{datetime.timestamp(now)}"
            self.slug = slugify(slug, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='attributes_of_product'
    )
    color = models.CharField(max_length=50, blank=True,  null=True)
    size = models.CharField(max_length=50, blank=True,  null=True)

    def __str__(self):
        return f"{self.id} - {self.product.name}"


    class Meta:
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"


class ProductPrice(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='prices_of_product'
    )
    price = models.PositiveIntegerField(default=0)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.id} - {self.product.name}"


    class Meta:
        verbose_name = "Product Price"
        verbose_name_plural = "Product Prices"

