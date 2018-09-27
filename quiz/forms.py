from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('Quiz_id', 'name', 'Test_Password', 'about', 'instructions', 'csv_file', 'positive', 'negative', 'duration')

        widgets = {
            'about': forms.Textarea(attrs={'class':'form-control col-11', 'cols': '10'}),
            'instructions': forms.Textarea(attrs={'class':'form-control col-11','cols': '10'}),
            'name' : forms.TextInput(attrs={'class':'form-control col-9'}),
            'Test_Password' :forms.TextInput(attrs={'type' : 'password','class':'form-control col-9'}),
            'positive' : forms.NumberInput(attrs = {'class':'form-control col-4'}),
            'negative' : forms.NumberInput(attrs = {'class':'form-control col-4'}),
            'duration' : forms.TimeInput(attrs = {'class':'form-control col-4'}),
            'Quiz_id': forms.TextInput(attrs={'class': 'form-control col-9'}),
            'csv_file': forms.FileInput(attrs={'class': 'form-control col-5 btn btn-primary btn-sm'})
            }
