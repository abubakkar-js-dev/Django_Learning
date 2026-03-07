from django import forms

class Registation(forms.Form):
    first_name = forms.CharField(max_length=75)
    last_name = forms.CharField(max_length=75)
    email = forms.EmailField(max_length=255)
    city = forms.CharField(max_length=120)
