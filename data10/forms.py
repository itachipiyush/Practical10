from django import forms
from data10.models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
