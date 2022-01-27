from django.db import models

# Create your models here.

#Supplier model
class Supplier(models.Model):
    # id automatically added
    supp_name = models.CharField(max_length=200)

    # make it more readable for testing
    def __str__(self):
        return self.supp_name
    
#Inventory model
class Inventory(models.Model):
    # id automatically added
    inv_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField() # added
    note = models.TextField(blank=True)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE) #on delete cascade -> corresponding rows from parent table will be deleted

    # thumbnail | source: https://www.youtube.com/watch?v=LAIVhl2CG8E&ab_channel=TheNetNinja
    thumbnail = models.ImageField(default='default.png', blank=True)
    
    # make it more readable for testing
    def __str__(self):
        return self.inv_name