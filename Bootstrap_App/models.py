from django.contrib.auth.models import User
from django.db import models

class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
    name = models.CharField(max_length=50)
    department = models.TextField()

    def __str__(self):
        return self.name

class Patients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    profession = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    patient_mobile = models.CharField(max_length=15)

    def __str__(self):
        return f"Appointment with Dr.{self.doctor_name} on {self.appointment_date}"
