from django.shortcuts import render
from ..models import Doctors,Patients,Appointment
# import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    doctors = Doctors.objects.all()
    total_doctors = len(doctors)
    patients = Patients.objects.all()
    total_patients = len(patients)
    return  render(request, 'index.html', {'doctors': doctors,'total_doctors':total_doctors,'total_patients':total_patients})
def about(request):
    return render(request, 'about.html')
# @login_required()
# def appointment(request):
#     doctors = Doctors.objects.all()
#     return render(request, 'appointment.html', {'doctors': doctors})
def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')
def home_page(request):
    return render(request, 'home_page.html')



