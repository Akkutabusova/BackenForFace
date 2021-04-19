from django.urls import path, include
from .views import UserViewSet,UserAPIView,\
    UserDetails,QRAPIView,QRDetails,DoorDetails,DoorAPIView, Inside

from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('user',UserViewSet,basename='user')


urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('user/',UserAPIView.as_view()),#classbased apiview
    path('qr/',QRAPIView.as_view()),
    path('door/',DoorAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('user/<int:id>/',UserDetails.as_view()),
    path('qr/<int:id>/',QRDetails.as_view()),
    path('door/<int:id>/',DoorDetails.as_view()),
    path('inside/',Inside.as_view()),
    #path('generic/article/<int:id>',GenericAPIView.as_view()),

]


