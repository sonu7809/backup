from django import forms 

class StudentRregistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()