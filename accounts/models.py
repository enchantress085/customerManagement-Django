from django.db import models

# Create your models here
class Customer(models.Model):
    name = models.CharField(max_length = 200, null=True)
    phone = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
    CATAGORY = (
            ('Indor','Indor'),
            ('Out door','Out door'),
    )
    name = models.CharField(max_length = 200, null=True)
    price = models.FloatField(null=True)
    catagory = models.CharField(max_length = 200, null=True, choices=CATAGORY)
    description = models.CharField(max_length = 200, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True)
    tags = models.ManyToManyField(Tag)




class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for deleviry','Out for deleviry'),
        ('Delevired','Delevired'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null=True)
    status = models.CharField(max_length = 200, null=True, choices=STATUS)