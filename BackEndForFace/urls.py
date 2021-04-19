from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from BackEndForFace import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('article/', views.articleList.as_view()),
    path('api/',include('back_for_face.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
