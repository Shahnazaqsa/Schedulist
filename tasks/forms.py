from django import forms
from .models import Todo

class TodoRegistration(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title' , 'description', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

