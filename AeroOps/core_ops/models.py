from django.db import models


# Create your models here.
class Aircraft(models.Model):
    registration = models.CharField(max_length=15)
    type = models.CharField(max_length=4)
    size = models.CharField(max_length=10)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id_number = models.IntegerField()
    role = models.CharField(max_length=3)
    workplace = models.CharField(max_length=4)
    shift = models.IntegerField()


class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    flight_created_timestamp = models.DateTimeField(auto_now_add=True)
    estimated_time_arrival = models.DateTimeField(default=None, null=True)
    estimated_time_departure = models.DateTimeField(default=None, null=True)
    actual_time_arrival = models.DateTimeField(default=None, null=True)
    actual_time_departure = models.DateTimeField(default=None, null=True)


class Service(models.Model):
    service_name = models.CharField(max_length=25)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
    ordered_timestamp = models.DateTimeField(auto_now_add=True)
    in_progress_timestamp = models.DateTimeField(default=None, null=True)
    completed_timestamp = models.DateTimeField(default=None, null=True)
