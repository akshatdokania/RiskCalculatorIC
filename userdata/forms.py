from django.forms import ModelForm
from .models import Userdata

class Userform(ModelForm):
    class Meta:
        model = Userdata
        fields = '__all__'
