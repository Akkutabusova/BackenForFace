from django.db import models
from django.db.models import ManyToManyField

from django.db import models
from django.db.models import ManyToManyField
from passlib.hash import pbkdf2_sha256

class User(models.Model):
    STATUS=(
        ('В помещении','В помещении'),
        ('Вне помещении', 'Вне помещении'),
    )
    name=models.CharField(max_length=200,null=True)
    surname=models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True,unique=True)
    password = models.CharField(max_length=256,null=True)
    images=models.ImageField(blank=False,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True, choices=STATUS,default=STATUS[1][1])

    #images=files[]

    def __str__(self):
        return  self.surname+" "+self.name

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password,self.password)

class Manager(models.Model):

    name=models.CharField(max_length=200,null=True)
    surname=models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    #images=files[]

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
    qr_string=models.CharField(max_length=100,null=False)
    #door_id=models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return  self.qr_string

class Inside(models.Model):
    user_id=models.IntegerField(null=False)
    entry_time=models.DateTimeField(auto_now_add=True,null=True)

    #images=files[]

    def __str__(self):
        return  self.user_id

