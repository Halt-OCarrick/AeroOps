from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AircraftViewSet, EmployeeViewSet, FlightViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'aircraft', AircraftViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]