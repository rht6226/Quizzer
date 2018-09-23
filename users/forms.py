from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control col-3'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control col-3'}),
            'email' : forms.TextInput(attrs={'class':'form-control col-3'}),
            }

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('DOB', 'college', 'bio', 'profilepic')

        widgets = {
            'DOB': DateInput(attrs={'class': 'form-control col-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control col-8'}),
            'college' : forms.TextInput(attrs={'class':'form-control col-6'}),
            }
