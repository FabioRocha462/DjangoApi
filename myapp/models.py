from django.db import models
#my imports

from users.models import User

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    validity = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    bidding_value = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
class Sale(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produtc + str(self.created_at)


class Pay(models.Model):

    name = models.CharField(max_length=255)
    value = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
