from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.viewsets import MongoEngineViewSet

router = DefaultRouter()
router.register(r'mymodel', MongoEngineViewSet, basename='mymodel')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
