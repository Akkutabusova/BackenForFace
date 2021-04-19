from django.shortcuts import render


from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User,QR,Door
from .serializers import UserSerializer,QRSerializer,DoorSerializer, InsideSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, )

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QRAPIView(APIView):
    def get(self,request):
        qrs = QR.objects.all()
        serializer = QRSerializer(qrs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = QRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoorAPIView(APIView):
    def get(self,request):
        users = Door.objects.all()
        serializer = DoorSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DoorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    def get_object(self,id):
        try:
            return User.objects.get(id=id)

        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        user=self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self,request,id):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QRDetails(APIView):
    def get_object(self,id):
        try:
            return QR.objects.get(id=id)

        except QR.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        qr=self.get_object(id)
        serializer = QRSerializer(qr)
        return Response(serializer.data)

    def put(self,request,id):
        qr = self.get_object(id)
        serializer = QRSerializer(qr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        qr = self.get_object(id)
        qr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DoorDetails(APIView):
    def get_object(self,id):
        try:
            return Door.objects.get(id=id)

        except User.DoesNotExist:
            return HttpResponse({'message': 'Page not found'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        user=self.get_object(id)
        serializer = DoorSerializer(user)
        return Response(serializer.data)

    def put(self,request,id):
        user = self.get_object(id)
        serializer = DoorSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, {'message': 'Try to scan face again'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Inside(APIView):
    permission_classes = (AllowAny, )#(IsAuthenticated,)

    def get(self, request):
        user=User.objects.all()#filter(is_superuser=False)
        serializer = InsideSerializer(user, many=True)
        return Response(serializer.data)