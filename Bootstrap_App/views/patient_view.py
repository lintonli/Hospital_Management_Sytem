from ..models import Patients
from django.shortcuts import render

def patient_detail (request, patient_id):
    patient = Patients.objects.get(id=patient_id)
    return render(request, 'patient_details.html', {'patient': patient})