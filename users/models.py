from django.db import models
from django import forms
from django.forms import widgets
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime, os



# USER_ROLE = (
#    ('Q', 'Quizzer'),
#    ('M', 'Quizmaster')
# )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to = 'profile/', blank=True)
    DOB = models.DateField(('Date'), default= datetime.date.today)
    college = models.CharField(max_length = 50)
    # degree = models.CharField(max_length =30)
    bio = models.TextField()
# class role(forms.ModelForm):
#     role= forms.ChoiceField(widget=forms.RadioSelect, choices=USER_ROLE)

    def __str__(self):
        return self.user.username

    @property
    def image_url(self):
        if self.profilepic:
            return self.profilepic.url
        else:
            return r"/static/user.png"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

