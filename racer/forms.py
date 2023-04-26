from django import forms
from .models import RaceTime


class RaceTimeForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=50)
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    time_in_seconds = forms.CharField(label='Time in Seconds', max_length=20)

    class Meta:
        model = RaceTime
        fields = ['name', 'phone_number', 'time_in_seconds']
