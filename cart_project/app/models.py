from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField()
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventory(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    PENDING = 'P'
    SHIPPING = 'S'
    COMPLETE  = 'C'

    ORDER_STATUS_CHOICES = [
        (PENDING,  'pending'),
        (COMPLETE,  'complete'),
        (SHIPPING,  'shipping')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=ORDER_STATUS_CHOICES, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
