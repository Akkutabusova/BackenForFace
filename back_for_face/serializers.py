from rest_framework import serializers
from .models import User, QR,Door
'''
class articleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()


    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.author)
        instance.email=validated_data.get('email',instance.email)
        instance.date=validated_data.get('date',instance.date)
        instance.save()
        return instance
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        #fields=['id','title','author','email']
        fields='__all__'

class QRSerializer(serializers.ModelSerializer):
    class Meta:
        model=QR
        #fields=['id','title','author','email']
        fields='__all__'

class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Door
        #fields=['id','title','author','email']
        fields='__all__'

class InsideSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','surname']
        #fields='__all__'