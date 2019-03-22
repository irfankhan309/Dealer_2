from django.db import models

# Create your models here.

class PostEnquiry(models.Model):
    Name=models.CharField(max_length=40)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    Vehicle=models.CharField(max_length=40)
    BIKE_Model=models.CharField(max_length=35)
    Color=models.CharField(max_length=35)
    Contact_Number=models.CharField(max_length=15)

class Sale(models.Model):
    Name_Of_Bike=models.CharField(max_length=45)
    Image=models.FileField()
    Model=models.CharField(max_length=30)
    Color=models.CharField(max_length=30)
    Description=models.CharField(max_length=100, blank=True)
