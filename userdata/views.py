from django.shortcuts import render
from .forms import Userform
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def user_input(request):
    userform = Userform()
    return render(request, 'userdata/calculate.html',  {'userform': userform})
