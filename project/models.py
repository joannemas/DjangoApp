from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.title