from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'about', 'csv_file','Test_Password','Quiz_id')

        widgets = {
            'about': forms.Textarea(attrs={'class':'form-control col-8'}),
            'name' : forms.TextInput(attrs={'class':'form-control col-6'}),
            'Test_Password' :forms.TextInput(attrs={'type' : 'password','class':'form-control col-6'}),

            'Quiz_id': forms.TextInput(attrs={'class': 'form-control col-6'}),
            }
