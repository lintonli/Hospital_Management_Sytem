from django.urls import  path,include

from rest_framework.routers import DefaultRouter
from .views import (home,about,contact,service, user_login,register,doctor_dashboard,book_appointment, home_page)


urlpatterns= [
    path('',home_page,name='index'),

path('login/', user_login, name='login'),
    path('home/', home, name='home'),

    path('register/', register, name='register'),

    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('appointment/', book_appointment, name='appointment'),

    path('service/', service, name='service'),

]