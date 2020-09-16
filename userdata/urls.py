from django.urls import path

from . import views

app_name = 'userdata'
urlpatterns = [
    path('', views.user_input, name='userinput'),
]
