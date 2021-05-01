from django.db import models
from passlib.hash import pbkdf2_sha256
from django.contrib import auth
from django.contrib.auth.models import User

class User(models.Model):
    STATUS=(
        ('В помещении','В помещении'),
        ('Вне помещении', 'Вне помещении'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",null=True, blank=True)
    name=models.CharField(max_length=200,null=True)
    surname=models.CharField(max_length=200,null=True)
    #username = models.CharField(max_length=200,null=True,unique=True)
    #password = models.CharField(max_length=256,null=True)
    images=models.ImageField(blank=False,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True, choices=STATUS,default=STATUS[1][1])


    def __str__(self):
        return  str(self.id)+" "+self.surname+" "+self.name

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)

class Manager(models.Model):
    name=models.CharField(max_length=200,null=True)
    surname=models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True,unique=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return  self.surname+" "+self.name

class Door(models.Model):
    STATUS = (
        ('Открыто', 'Открыто'),
        ('Закрыто', 'Закрыто'),
    )
    door_name=models.CharField(max_length=200,null=True)
    qr_string=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True, choices=STATUS,default=STATUS[1][1])

    def __str__(self):
        return  self.door_name

class QR(models.Model):
    user_id=models.CharField(max_length=10,null=True)
    qr_string=models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return  self.qr_string

class Inside(models.Model):
    user_id=models.IntegerField(null=True)
    entry_time=models.DateTimeField(auto_now_add=True,null=True)
    door_id=models.IntegerField(null=True)

    #images=files[]

    def __str__(self):
        return  str(self.user_id)+" "+str(self.entry_time)

