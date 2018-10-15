from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('Quiz_id', 'name', 'Test_Password', 'about', 'instructions', 'csv_file', 'positive', 'negative', 'duration','tags')

        widgets = {
            'about': forms.Textarea(attrs={'class':'form-control col-8'}),
            'instructions': forms.Textarea(attrs={'class':'form-control col-8'}),
            'name' : forms.TextInput(attrs={'class':'form-control col-6'}),
            'Test_Password' :forms.TextInput(attrs={'type' : 'password','class':'form-control col-6'}),
            'positive' : forms.NumberInput(attrs = {'class':'form-control col-3'}),
            'negative' : forms.NumberInput(attrs = {'class':'form-control col-3'}),
            'duration' : forms.TimeInput(attrs = {'class':'form-control col-3'}),
            'Quiz_id': forms.TextInput(attrs={'class': 'form-control col-6'}),
            'csv_file': forms.FileInput(attrs={'class': 'form-control col-5 btn btn-primary btn-sm'}),
            'tags':forms.TextInput(attrs={'class': 'form-control col-6','placeholder':'Separate tags with comma(,)'}),
            }
