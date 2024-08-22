# forms.py
from django import forms
from .models import Student, Class

class AttendanceForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    class_attended = forms.ModelChoiceField(queryset=Class.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget)
    is_present = forms.BooleanField(required=False)
