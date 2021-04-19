from django.db import models
from django.db.models import ManyToManyField


class User(models.Model):
    STATUS=(
        ('В помещении','В помещении'),
        ('Вне помещении', 'Вне помещении'),
    )
    name=models.CharField(max_length=200,null=True)
    surname=models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    images=models.ImageField(blank=False,null=True)
    data_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True, choices=STATUS)

    #images=files[]

    def __str__(self):
        return  self.surname+" "+self.name

class Door(models.Model):
    door_name=models.CharField(max_length=200,null=True)


    def __str__(self):
        return  self.door_name

class QR(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    qr_string=models.CharField(max_length=100)
    door=models.ForeignKey(Door,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return  self.qr_string

