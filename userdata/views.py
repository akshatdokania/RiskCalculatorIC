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
            count, message = checkparams(request.POST)
            return render(request, 'userdata/result.html', {'count':count, 'message': message})
        else:
            errmsg = form.errors.as_data()
            return render(request, 'userdata/calculate.html', {'errmsg':errmsg})
    else:
        userform = forms.Userform()
    return render(request, 'userdata/calculate.html',  {'userform': userform})



def checkparams(params):
    total = 0
    total_param = 21
    count_epi = 0
    count_vital = 0
    count_lab = 0
    riskMessage = "Risk returned null"
    if int(params['age']) > 55:
        counter += 1
    if 'hpd' in params:
        count_epi += 1
    if 'ckd' in params:
        count_epi += 1
    if 'dm' in params:
        count_epi += 1
    if 'htn' in params:
        count_epi += 1
    if 'hiv' in params:
        count_epi += 1
    if 'trans' in params:
        count_epi +=  1
    if int(params['resrate']) > 24:
        count_vital += 1
    if int(params['heartrate']) > 125:
        count_vital += 1
    if int(params['spo']) < 90:
        count_vital += 1
    if int(params['ddimer']) != None and int(params['ddimer']) > 1000:
        count_lab += 1
    if int(params['cpk']) != None and int(params['cpk']) > 400:
        count_lab += 1
    if int(params['crp']) != None and int(params['crp']) > 100:
        count_lab += 1
    if int(params['ldh']) != None and int(params['ldh']) > 245:
        count_lab += 1
    if float(params['tropo']) != None and float(params['tropo']) > 0.1:
        count_lab += 1
    if int(params['ferr']) != None and int(params['ferr']) > 500:
        count_lab += 1
    if float(params['absolute']) != None and float(params['absolute']) < 0.8:
        count_lab += 1
    total = count_epi+count_lab+count_vital
    risk = (total/total_param) * 10
    risk = round(risk, 2)
    total_vl = count_lab+count_vital
    if(count_epi>0 and count_vital>0 and count_lab>0):
        riskMessage = "High Risk"
        return risk,riskMessage
    elif(tot_vl == 2 and count_lab != 0 and count_vital != 0):
        riskMessage = "Moderate Risk"
        return risk,riskMessage
    elif(tot_vl >= 2):
        riskMessage = "High Risk"
        return risk,riskMessage
    elif(count_epidem > 0 and (count_lab == 1 or count_vital == 1)):
        riskMessage = "Moderate Risk"
        return risk,riskMessage
    elif(total < 2 or (count_epidem > 0 and count_lab == 0 and count_vital == 0)):
        riskMessage = "Low Risk"
        return risk, riskMessage
    return risk,riskMessage
