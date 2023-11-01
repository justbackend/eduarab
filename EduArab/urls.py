from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app1.views import *
router = DefaultRouter()
router.register('javobview', JavobModelView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('savol/', SavolApi.as_view()),
    path('javob/', JavobApi.as_view()),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


