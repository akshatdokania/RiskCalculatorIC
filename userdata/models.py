from django.db import models

class Userdata(models.Model):
    name      = models.CharField(max_length=40, default='')      #name
    age       = models.IntegerField()   #agefield
    hpd       = models.BooleanField()   #history of pulmonary disease
    ckd       = models.BooleanField()   #history of ckd
    dm        = models.BooleanField()   #history of DM
    htn       = models.BooleanField()   #history of HTN
    hiv       = models.BooleanField()   #history of HIV
    trans     = models.BooleanField()   #immunosuppression/transplant
    resrate   = models.IntegerField()   #respiratory rate to be taken from electronics
    heartrate = models.IntegerField()   #heart rate to be taken from electronics
    spo       = models.IntegerField()   #spo2 to be taken from electronics
    ddimer    = models.IntegerField()   #ddimer ug/ml
    cpk       = models.IntegerField()   #cpk     U/L
    crp       = models.IntegerField()   #crp     mg/L
    ldh       = models.IntegerField()   #LDH     U/L
    tropo     = models.FloatField()     #tropopin ng/mL
    ferr      = models.IntegerField()   #ferritin ug/L
    absolute  = models.FloatField()     #Absolute Lymphocyte count
    ctscan    = models.IntegerField()   #CT SCAN
    abg       = models.IntegerField()   #ABG (P/F ratio)

    def __str__(self):
        return self.name
