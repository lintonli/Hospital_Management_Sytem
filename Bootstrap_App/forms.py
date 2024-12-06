from django import  forms
from django.contrib.auth.models import User

from .models import Appointment,Patients


class PatientsForm(forms.ModelForm):
    username= forms.CharField(max_length=100, required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)
    name= forms.CharField(max_length=100, required=True)
    gender= forms.ChoiceField(choices=(('M','Male'),('F','Female')),required=True)
    age= forms.IntegerField(required=True)
    profession=forms.CharField(max_length=100)

    class Meta:
        model=Patients
        fields=['name','gender','age','profession']

    def save(self, commit=True):
        # Create the User object first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        patient = super().save(commit=False)
        patient.user = user  # Associate the Patient with the newly created User
        if commit:
            patient.save()
        return patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'appointment_date']