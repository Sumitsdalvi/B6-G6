from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField()
    
    class meta:
        db_table = "Book"

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  

    class meta:
        db_table = "Employee"
  
    def __str__(self):  
        return f"{self.first_name}--{self.last_name}"  

class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    class meta:
        db_table = "Company"