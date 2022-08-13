from django import forms
from .models import ToDo

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class ToDoForm(forms.ModelForm):
    finishdate = forms.DateTimeField(widget = DateTimeInput)
    class Meta:
        model = ToDo
        fields = ('title', 'description') 