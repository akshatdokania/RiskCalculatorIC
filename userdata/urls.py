from django.urls import path

from . import views

app_name = 'userdata'
urlpatterns = [
    path('patienttype/', views.patienttype, name='patienttype'),
    path('userinput/', views.user_input, name='userinput'),
]
