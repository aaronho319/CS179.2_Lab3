from django.db import models

# Create your models here.

class AbstractClass(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now_add = True)

	class Meta:
		abstract = True

class User(AbstractClass):

    email = models.EmailField()
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    shippingAddress = models.TextField()

class Cart(AbstractClass):
    cart_code = models.CharField(max_length = 10)
    product = models.ManyToManyField(Product)
    hasPaid = models.BooleanField()

    def totalPrice(self, price):
    	product = Product()
    	price = price + product.price

class Product(AbstractClass):
    price = models.FloatField()
    name =  models.CharField(max_length = 50)
    description = models.TextField()

