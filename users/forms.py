from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('college', 'bio', 'profilepic')

    def clean_avatar(self):
        avatar = self.cleaned_data['profilepic']
        return avatar