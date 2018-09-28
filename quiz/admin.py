from django.contrib import admin

from .models import Quiz, Question, Answers,Score

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Score)