from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('quiz_id', 'name', 'quiz_password' , 'about', 'csv_file')

        widgets = {
            'quiz_id': forms.TextInput(attrs={'class': 'form-control col-6'}),
            'quiz_password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control col-6'}),
            'about': forms.Textarea(attrs={'class':'form-control col-8'}),
            'name' : forms.TextInput(attrs={'class':'form-control col-6'}),
            }