from rest_framework import viewsets
from core_ops.models import Aircraft, Employee, Flight, Service
from api.serializers import (
    AircraftSerializer,
    EmployeeSerializer,
    FlightListSerializer,
    FlightDetailSerializer,
    ServiceSerializer
)

class AircraftViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows aircraft to be viewed or edited.
    """
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    API enpoint that handles the creation of a flight.
    """
    queryset = Flight.objects.all().select_related('aircraft')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FlightDetailSerializer
        return FlightListSerializer  # Used for 'list' and 'create'


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that handles tracking services.
    Uses select_related to optimize the foreign key lookup to Employee.
    """
    queryset = Service.objects.all().select_related('assigned_employee')
    serializer_class = ServiceSerializer