from django.shortcuts import render


from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User,QR,Door,Inside, Manager
from .serializers import UserSerializer,QRSerializer,DoorSerializer,InsideSerializer, ManagerSerializer
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

from passlib.hash import pbkdf2_sha256
import os

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserAPIGetView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if (serializer.is_valid()):
            if (checkNumber(request.data['phone'])):
                serializer.save()
                user_hashpassword=User.objects.get(id=serializer.data['id'])
                hash=pbkdf2_sha256.encrypt(serializer.data['password'], rounds=12000, salt_size=32)
                serializer_hashpassword = UserSerializer(user_hashpassword, data={"password":hash})
                if serializer_hashpassword.is_valid():
                    serializer_hashpassword.save()
                    return Response(serializer_hashpassword.data, status=status.HTTP_201_CREATED)
                    #return Response("User created successfully", status=status.HTTP_201_CREATED)
            else:
                return Response("Wrong phone format", status=status.HTTP_400_BAD_REQUEST)
            #return HttpResponse(str(new_data))
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Wrong format of data", status=status.HTTP_400_BAD_REQUEST)

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
        try:
            if (request.data['phone'] != None and checkNumber(request.data['phone'])==False):
                return Response("Wrong phone format", status=status.HTTP_400_BAD_REQUEST)
        except:
            print("there is no phone, contiue")
        if serializer.is_valid():

            serializer.save()
            if (serializer.data['password'] != None):
                user_hashpassword = User.objects.get(id=serializer.data['id'])
                hash = pbkdf2_sha256.encrypt(serializer.data['password'], rounds=12000, salt_size=32)
                serializer_hashpassword = UserSerializer(user_hashpassword, data={"password": hash})
                if serializer_hashpassword.is_valid():
                    serializer_hashpassword.save()
                    return Response(serializer_hashpassword.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#------------------

class ManagerAPIView(APIView):
    def get(self,request):
        users = Manager.objects.all()
        serializer = ManagerSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagerAPIGetView(APIView):
    def get(self,request):
        users = Manager.objects.all()
        serializer = ManagerSerializer(users, many=True)
        return Response(serializer.data)
#--------------------------------


class QRAPIGetView(APIView):
    def get(self,request):
        qrs = QR.objects.all()
        serializer = QRSerializer(qrs, many=True)
        return Response(serializer.data)

class QRAPIView(APIView):
    def get(self,request):
        qrs = QR.objects.all()
        serializer = QRSerializer(qrs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = QRSerializer(data=request.data)

        if serializer.is_valid():
            cmd = "python C:/Users/Malika/Desktop/technodom/technodom/1/deep-face-real-time.py "+str(request.data['user_id'])
            returned_value=os.system(cmd)
            door = Door.objects.get(qr_string=request.data['qr_string'])
            user=User.objects.get(id=request.data['user_id'])
            serializer_user=UserSerializer(user)
            serializer_door = DoorSerializer(door)
            if(returned_value==0):
                serializer.save()
                #------------------
                serializer_opendoor = DoorSerializer(door, data={"status":"Открыто"})
                if serializer_opendoor.is_valid():
                    serializer_opendoor.save()

                #DoorDetails.change_status(serializer_door.data['id'],"Открыто")
                return Response("Open "+serializer_door.data['door_name']+". It is "+serializer_user.data["name"],
                                status=status.HTTP_200_OK)
            else:
                return Response("Don't open "+serializer_door.data['door_name']+". It is not "+serializer_user.data["name"],
                                status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------
class InsideAPIView(APIView):
    def get(self,request):
        users = Inside.objects.all()
        serializer = InsideSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = InsideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InsideDetails(APIView):
    def get_object(self,id):
        try:
            return Inside.objects.get(id=id)

        except Inside.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        user=self.get_object(id)
        serializer = InsideSerializer(user)
        return Response(serializer.data)

    def put(self,request,id):
        user = self.get_object(id)
        serializer = InsideSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#----------------------

class DoorAPIView(APIView):
    def get(self,request):
        users = Door.objects.all()
        serializer = DoorSerializer(users, many=True)
        return Response(serializer.data)

    '''def post(self,request):
        serializer = DoorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

class DoorDetails(APIView):
    def get_object(self,id):
        try:
            return Door.objects.get(id=id)

        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        user=self.get_object(id)
        serializer = DoorSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        door = self.get_object(id)
        serializer = DoorSerializer(door, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, {'message': 'Try to scan face again'}, status=status.HTTP_400_BAD_REQUEST)

    '''
    def change_status(self,id,string_status):
        door = self.get_object(id)
        serializer = DoorSerializer(door, data={"status":string_status})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, {'message': 'Try to scan face again'},
                            status=status.HTTP_400_BAD_REQUEST)
   

    def delete(self,request,id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

#---------------------

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
        return Response(serializer.errors, {'message': 'Try to scan face again'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        qr = self.get_object(id)
        qr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def checkNumber(number):
    if(number[0]=="8"):
        if(len(number)==11):
            if(number[1]=="7"):
                print(number[1])
                return True
    elif(number[0:2]=="+7"):
        if(len(number)==12):
            if(number[2]=="7"):
                return True
    return False