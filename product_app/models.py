from django.db import models

# Create your models here.

class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_cat= models.CharField(max_length=100)
    prod_price = models.FloatField()
    prod_qty= models.IntegerField()
    prod_img = models.ImageField(upload_to = 'products/',default='default.jpg')
    prod_desc = models.CharField(max_length=100)
def __str__(self):
    return self.prod_name
