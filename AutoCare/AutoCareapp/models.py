from django.db import models

# Create your models here.

# transport_admin module
class TransportAdmin (models.model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    GENDER_CHOICES ={
        ('M', 'male'),
        ('F', 'female'),
         }
    gender = models.CharField(max_length=1,choices = GENDER_CHOICES, default ='M')
    
    def__str__(self)
    return f"{self.name}({self.email})"

#Car module
class Car(models.Model):
    admin = models.ForeignKey(TransportAdmin, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def__str__(self)
    return f"{self.name}({self.plate_number})"

#Task module (garager)
class Task(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('Service', 'Service'),
        ('Repairs', 'Repairs'),
    ]
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def__str__(self)
    return f"{self.name}({self.service_type} - {self.car.plate_number})"

    #payment module(accoutant)
class Payment(models.Model):
    service = models.ManyToOneRel(Task, on_delete=models.CASCADE, related_name='payment')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def__str__(self)
    return f"Payment for{self.service.service_type}"