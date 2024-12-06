from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.shortcuts import redirect, render
from ..models import Doctors,Appointment, Patients
from ..forms import AppointmentForm

@login_required(login_url='login')
def book_appointment(request):
        # Ensure the logged-in user is a patient
        if not hasattr(request.user, 'patients'):
            return render(request, 'login.html', {'message': 'You are not authorized to book an appointment.'})

        patient = request.user.patients  # Get the logged-in patient's profile
        doctors = Doctors.objects.all()  # Fetch all available doctors

        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():

                appointment = form.save(commit=False)
                appointment.patient_name = patient
                appointment.patient_mobile = patient.mobile
                appointment.save()


                messages.success(request, f'Your appointment has been booked successfully!')
                return redirect('home')
        else:
            form = AppointmentForm()

        return render(request, 'appointment.html', {'form': form, 'doctors': doctors})

