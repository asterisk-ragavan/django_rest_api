from django.db import models

class store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    barcode=models.IntegerField()
    store=models.ForeignKey(store,on_delete=models.CASCADE,related_name="items")

    def __str__(self):
        return self.name
    