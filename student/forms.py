from django import forms

from bootstrap_daterangepicker import widgets, fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LogInForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=30)

    class Meta:
        model = Faculty
        fields = ['username', 'password']


class StudentLookUpForm(forms.ModelForm):
    student = forms.ModelChoiceField( queryset=Student.objects.all(),required=True)

    class Meta:
        model = Student
        fields = ['id']


class DateRangeForm(forms.Form):
    date =fields.DateRangeField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DateRangeWidget(
            format='%d/%m/%Y'
        ),clearable=True
    )

