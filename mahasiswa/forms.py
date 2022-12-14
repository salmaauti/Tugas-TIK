from django.forms import ModelForm
from django import forms
from mahasiswa.models import Mahasiswa

class FormMahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        exclude = ['foto']

        widgets = {
            'no' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Nomor Absen'}),
            'nama' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama'}),
            'nim' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nim'}),
            'ttl' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tempat Tanggal Lahir'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

    
        
     