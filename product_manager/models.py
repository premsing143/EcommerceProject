from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()

    def __str__(self):
        return(self.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()  

    def __str__(self):
        return(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500, null=True)
    color_code = models.CharField(max_length=20, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    registered_on = models.DateTimeField(null=True)
    is_active = models.BooleanField(null=True)

    def image_tag(self):
        return mark_safe(f'<img src="{self.image_url}"width="50" height="50"/>')
          
    def __str__(self):
        return(self.name)

class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entered_on = models.DateTimeField()      
