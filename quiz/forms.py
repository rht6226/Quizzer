from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'about', 'csv_file')

        widgets = {
            'about': forms.Textarea(attrs={'class':'form-control col-8'}),
            'name' : forms.TextInput(attrs={'class':'form-control col-6'}),
            }