from django.contrib.auth.decorators import login_required
from django.shortcuts import  render
from ..models import  Appointment

# def doctor_list(request):
#     doctors = Doctors.objects.all()
#     return render(request, 'index.html', {'doctors': doctors})
@login_required(login_url='login')
def doctor_dashboard(request):
    # patients = Patients.objects.all()
    # return render(request, 'doctor_dashboard.html', {'patients': patients})
    if not hasattr(request.user, 'doctors'):
        return render(request, 'login.html', {'message': 'You are not authorized to view this page.'})

    doctor = request.user.doctors  # The logged-in doctor's profile
    appointments = Appointment.objects.filter(doctor_name=doctor)  # Filter appointments for the logged-in doctor

    return render(request, 'doctor_dashboard.html', {'appointments': appointments})