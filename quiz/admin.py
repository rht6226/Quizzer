from django.contrib import admin

from .models import Quiz, Question, Answers

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answers)