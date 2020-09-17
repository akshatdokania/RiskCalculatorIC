from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def user_input(request):
    if request.method == 'POST':
        form = forms.Userform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('userdata:userinput')
    userform = forms.Userform()
    return render(request, 'userdata/calculate.html',  {'userform': userform})
