from django.contrib.auth.decorators import login_required
from django.shortcuts import  render,redirect
from django.contrib import messages
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
    appointments = Appointment.objects.filter(doctor_name=doctor).select_related('patient_name')  # Filter appointments for the logged-in doctor

    return render(request, 'doctor_dashboard.html', {'appointments': appointments})

# def cancel_appointment(request, appointment_id):
#     if not hasattr(request.user, 'doctors'):
#         return render(request, 'login.html', {'message': 'You are not authorized to view this page.'})
#     appointment = Appointment.objects.get(id=appointment_id, doctor_name=request.user.doctors)
#     appointment.delete()
#     messages.success(request, 'Appointment deleted successfully.')
#     return redirect('doctor_dashboard')

def cancel_appointment(request, appointment_id):
    # Ensure the user is a doctor
    if not hasattr(request.user, 'doctors'):
        messages.error(request, "You are not authorized to cancel appointments.")
        return redirect('doctor_dashboard')


    try:
        appointment = Appointment.objects.get(id=appointment_id, doctor_name=request.user.doctors)
        appointment.delete()
        messages.success(request, "The appointment has been successfully canceled.")
    except Appointment.DoesNotExist:
        messages.error(request, "The appointment does not exist or you are not authorized to cancel it.")

    return redirect('doctor_dashboard')