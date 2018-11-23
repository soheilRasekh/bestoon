from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class UserRegisterTemp(models.Model):
    username    = models.CharField(max_length=255)
    password    = models.CharField(max_length=255)    
    email       = models.CharField(max_length=255)
    code        = models.CharField(max_length=255) 

class Token(models.Model):
    token = models.CharField(max_length= 255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}-token".format(self.user)


class Expense(models.Model):
    text    = models.CharField(max_length = 255)
    date    = models.DateTimeField(default=timezone.now())
    amount  = models.BigIntegerField()
    user    = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.date,self.amount)

class Income(models.Model):
    text    = models.CharField(max_length = 255)
    date    = models.DateTimeField(default=timezone.now())
    amount  = models.BigIntegerField()
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)