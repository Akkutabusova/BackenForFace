from django.urls import path, include
from .views import UserViewSet,UserAPIView,\
    UserDetails,QRAPIView,QRDetails,DoorDetails,DoorAPIView ,UserAPIGetView,\
QRAPIGetView,UserIndoorAPIView,UserIndoorDetails,ManagerAPIView
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('user',UserViewSet,basename='user')


urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('registration/',UserAPIView.as_view()),#classbased apiview
    path('auth/',QRAPIView.as_view()),
    path('door/',DoorAPIView.as_view()),
    path('manager/',ManagerAPIView.as_view()),
    path('inside/',UserIndoorAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('update/user/<int:id>/',UserDetails.as_view()),
    path('update/inside/<int:id>/',UserIndoorDetails.as_view()),
    path('user/', UserAPIGetView.as_view()),
    path('qr/', QRAPIGetView.as_view()),
    path('update/auth/<int:id>/',QRDetails.as_view()),
    path('door/<int:id>/',DoorDetails.as_view()),
    #path('generic/article/<int:id>',GenericAPIView.as_view()),

]


