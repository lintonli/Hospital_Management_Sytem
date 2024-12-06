from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render

from ..forms import PatientsForm
from django.http import  HttpResponse

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)


            if hasattr(user, 'doctors'):
                return redirect('doctor_dashboard')
            elif hasattr(user, 'patients'):
                return redirect('home')
            else:

                messages.error(request, "You are not authorized to access this page.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    # messages.success(request, "Login successful")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PatientsForm()
    return render(request, 'register.html', {'form': form})
