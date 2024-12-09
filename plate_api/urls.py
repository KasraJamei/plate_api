from django.urls import path, include
from rest_framework.routers import DefaultRouter

#importing views form local views.py
from .views import index
from .views import VehicleViewSet, LicenseViewSet, TrafficHistoryViewSet, VehiclePlateRecognitionViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'licenses', LicenseViewSet)
router.register(r'traffic-history', TrafficHistoryViewSet)
router.register(r'recognize-plate', VehiclePlateRecognitionViewSet, basename='recognize-plate')


urlpatterns = [
    path("", index, name="home"),
    path('api/', include(router.urls)),
     
]
