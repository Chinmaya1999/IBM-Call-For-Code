from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

class Userinfo(models.Model):
    username=models.CharField(max_length=300,null=True)
    firstname=models.CharField(max_length=300,null=True)
    lastname=models.CharField(max_length=300,null=True)
    email=models.CharField(max_length=300,null=True)
    password=models.CharField(max_length=300,null=True)
    phone=models.CharField(max_length=300,null=True)
    address=models.CharField(max_length=300,null=True)
    pin=models.CharField(max_length=6,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

class DonatedFood(models.Model):
    TYPES=(('Uncooked','Uncooked'),('Cooked','Cooked'))
    no=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    foodStatus=models.CharField(max_length=200,null=True,choices=TYPES)
    foodDescription=models.CharField(max_length=500,null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.foodDescription

class DonatedCloth(models.Model):
    TYPES=(('Male','Male'),('Female','Female'))
    no=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    clothType=models.CharField(max_length=200,null=True,choices=TYPES)
    clothDescription=models.CharField(max_length=500,null=True)
    timestamp = models.DateTimeField(default=now)
    # def __str__(self):
        # return self.

class DistributionCentre(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=300,null=True)
    pin=models.CharField(max_length=6,null=True)
    phone=models.CharField(max_length=30,null=True)
    administrator=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

class foodDonation(models.Model):
    TYPES=(('Pending','Pending'),('Accepted','Accepted'))
    distributionCentre=models.ForeignKey(DistributionCentre,null=True,on_delete=models.SET_NULL)
    donatedFood=models.ForeignKey(DonatedFood,null=True,on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(default=now)
    status=models.CharField(max_length=200,null=True,choices=TYPES)
    # def __str__(self):
        # return self.timestamp
class clothDonation(models.Model):
    TYPES=(('Pending','Pending'),('Accepted','Accepted'))
    distributionCentre=models.ForeignKey(DistributionCentre,null=True,on_delete=models.SET_NULL)
    donatedCloth=models.ForeignKey(DonatedCloth,null=True,on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(default=now)
    status=models.CharField(max_length=200,null=True,choices=TYPES)
    # def __str__(self):
        # return self.timestamp
