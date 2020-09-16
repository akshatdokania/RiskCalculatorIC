from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

#user login view for sign up or login
def login_view(request):
    if request.method == 'POST':
        if request.POST.get('login') == 'login':
            form=AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return  redirect('userdata:userinput')
            else:
                authform = AuthenticationForm()
        if request.POST.get('signup')== 'signup':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return  redirect('userdata:userinput')
            else: userform = UserCreationForm()
    else:
        authform = AuthenticationForm()
        userform = UserCreationForm()
        return  render(request, 'accounts/login.html', {'authform': authform, 'userform' : userform})

#logging out users
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('')
