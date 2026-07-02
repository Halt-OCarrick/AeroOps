from rest_framework import serializers
from core_ops.models import Aircraft, Employee, Flight, Service

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'registration', 'type', 'size']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'employee_id_number', 'role', 'workplace', 'shift']


class ServiceSerializer(serializers.ModelSerializer):
    assigned_employee_detail = EmployeeSerializer(source='assigned_employee', read_only=True)
    assigned_employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Service
        fields = [
            'id', 'service_name', 'flight', 'assigned_employee',
            'assigned_employee_detail', 'ordered_timestamp',
            'in_progress_timestamp', 'completed_timestamp'
        ]


class FlightListSerializer(serializers.ModelSerializer):
    aircraft = serializers.SlugRelatedField(
        slug_field='registration',
        queryset=Aircraft.objects.all(),
    )

    class Meta:
        model = Flight
        fields = [
            'id', 'aircraft',
            'estimated_time_arrival', 'estimated_time_departure',
            'actual_time_arrival', 'actual_time_departure'
        ]


class FlightDetailSerializer(serializers.ModelSerializer):
    aircraft = serializers.SlugRelatedField(
        slug_field='registration',
        queryset=Aircraft.objects.all()
    )
    services = ServiceSerializer(many=True, read_only=True, source='service_set')

    class Meta:
        model = Flight
        fields = [
            'id', 'aircraft', 'estimated_time_arrival',
            'estimated_time_departure', 'actual_time_arrival',
            'actual_time_departure', 'services'
        ]