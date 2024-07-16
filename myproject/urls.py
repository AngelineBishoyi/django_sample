from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.viewsets import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet, basename='mymodel')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
