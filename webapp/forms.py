from django import forms
from django.core.exceptions import ValidationError
from webapp.models import student

class loginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)


class studentForm(forms.ModelForm):

    gn = (

        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect())
    is_active = forms.CharField(widget=forms.CheckboxInput())
    class Meta:
        model = student
        fields=('first_name','middle_name','last_name','email','address','gender','is_active')
        # fields = ('email', 'address')



