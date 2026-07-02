from django.db import models


# Create your models here.
class Aircraft(models.Model):
    registration = models.CharField()
    type = models.CharField()
    size = models.CharField()


class Employee(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    employee_id_number = models.IntegerField()
    role = models.CharField()
    workplace = models.CharField()
    shift = models.IntegerField()


class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    estimated_time_arrival = models.DateTimeField()
    estimated_time_departure = models.DateTimeField()
    actual_time_arrival = models.DateTimeField()
    actual_time_departure = models.DateTimeField()


class Service(models.Model):
    service_name = models.CharField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
    ordered_timestamp = models.DateTimeField()
    in_progress_timestamp = models.DateTimeField()
    completed_timestamp = models.DateTimeField()
