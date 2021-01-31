from django.db import models

# Create your models here.
##just create model
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

#### to return the value you want to return in frontend
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    ### to write diffrent categories we write as
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    ##many to many relationship
    tag = models.ManyToManyField(Tag, null=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)
    # tag=models.ManyToManyField(Tag, null=True)
    STATUS = (
        ('pending','pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200,null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
