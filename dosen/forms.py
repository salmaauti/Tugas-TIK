from django.forms import ModelForm
from django import forms
from dosen.models import Dosen

class FormDosen(forms.ModelForm):
    class Meta:
        model = Dosen
        exclude = ['foto']

        widgets = {
            'no' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'No'}),
            'nip' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nip'}),
            'nama' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama'}),
            'jabatan' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jabatan'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

    
        
     