from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Cart(models.Model):
    items = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Cart {self.total}"
    
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.URLField()
    age = models.PositiveIntegerField()
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='customer')

    def __str__(self):
        return f"Customer {self.name} {self.surname}"
    

class Manager(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.URLField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"Manager {self.name} {self.surname}"

class DeliveryCrew(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.URLField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"DeliveryCrew {self.name} {self.surname}"