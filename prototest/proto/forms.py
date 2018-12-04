from django import forms

class parentForm(forms.Form):
    name = forms.CharField
    email = forms.EmailField