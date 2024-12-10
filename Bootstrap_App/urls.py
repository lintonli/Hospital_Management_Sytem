from django.urls import  path,include
from .views import (home,about,contact,service, cancel_appointment, user_login,register,user_logout,doctor_dashboard,book_appointment, home_page,patient_detail)


urlpatterns= [
    path('',home_page,name='index'),

path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),

    path('register/', register, name='register'),

    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient_detail/<int:patient_id>/', patient_detail, name='patient_detail'),
    path('cancel_appointment/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('appointment/', book_appointment, name='appointment'),

    path('service/', service, name='service'),

]