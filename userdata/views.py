from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required
from .models import Userdata

@login_required(login_url="/accounts/login/") #login check
def patienttype(request):
    return render(request, 'userdata/patienttype.html')

 #input form
def user_input(request):
    if request.method == 'POST':
        if 'patient' in request.POST.keys():
            if request.POST.get('patient') == 'existing':   #checking if existing patient requested
                id = request.POST.get('hospitalid')
                try:
                    queryform = Userdata.objects.get(hospitalid = id)
                    userform = forms.Userform(instance=queryform)
                    return render(request, 'userdata/calculate.html', {'userform':userform})
                except Exception as errmsg:
                    return render(request, 'userdata/patienttype.html', {'errmsg': errmsg})
            if request.POST.get('patient') == 'new':        #checks for new patient
                id = request.POST.get('hospitalid')
                try:
                    queryform = Userdata.objects.get(hospitalid = id)
                    errmsg = "ID already exists"
                    return render(request, 'userdata/patienttype.html', {'errmsg':errmsg})
                except:
                    userform = forms.Userform(initial={'hospitalid': id})
                    return render(request, 'userdata/calculate.html', {'userform': userform})

        model, created = Userdata.objects.get_or_create(hospitalid = request.POST.get('hospitalid'))
        form = forms.Userform(request.POST, instance = model)
        if form.is_valid():
            form.save()
            count = checkparams(request.POST)
            return render(request, 'userdata/result.html', {'count':count})
        else:
            return HttpResponse(form.errors.as_data())
    else:
        userform = forms.Userform()
    return render(request, 'userdata/calculate.html',  {'userform': userform})



def checkparams(params):
    counter = 0
    if int(params['age']) > 55:
        counter += 1
    if 'hpd' in params:
        counter += 1
    if 'ckd' in params:
        counter += 1
    if 'dm' in params:
        counter += 1
    if 'htn' in params:
        counter += 1
    if 'hiv' in params:
        counter += 1
    if 'trans' in params:
        counter +=  1
    if int(params['resrate']) > 24:
        counter += 1
    if int(params['heartrate']) > 125:
        counter += 1
    if int(params['spo']) < 90:
        counter += 1
    if int(params['ddimer']) > 1000:
        counter += 1
    if int(params['cpk']) > 400:
        counter += 1
    if int(params['crp']) > 100:
        counter += 1
    if int(params['ldh']) > 245:
        counter += 1
    if float(params['tropo']) > 0.1:
        counter += 1
    if int(params['ferr']) > 500:
        counter += 1
    if float(params['absolute']) < 0.8:
        counter += 1
    return counter
