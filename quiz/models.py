from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Quiz(models.Model):
    name = models.CharField(max_length = 50)
    csv_file = models.FileField(upload_to='quizzes/csv/')
    about = models.TextField(max_length= 2000)
    Test_Password = models.CharField(max_length=50,default='')
    quizmaster =   models.ForeignKey(User, on_delete= models.CASCADE)
    instructions = models.TextField(default=' ')
    Quiz_id = models.CharField(max_length=50,default='')
    positive = models.IntegerField(default=3)
    negative = models.IntegerField(default=1)
    duration = models.DurationField(default= timedelta())

    def __str__(self):
            return self.name

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.TextField(max_length=2000)
    a = models.CharField(max_length= 500)
    b = models.CharField(max_length= 500)
    c = models.CharField(max_length= 500)
    d = models.CharField(max_length= 500)
    correct = models.CharField(max_length= 500)
    image = models.URLField(default= "")
    code = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        title = self.question[:40]
        return title

class Answers(models.Model):
    applicant = models.ForeignKey(User, on_delete= models.CASCADE ) 
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    response = models.CharField(max_length=500, default='')
    correct_choice = models.CharField(max_length=500)

class Score(models.Model):
    applicant = models.ForeignKey(User, on_delete= models.CASCADE ) 
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    obtained = models.IntegerField(default=0)
    total = models.IntegerField(default= 0)

    def __str__(self):
        title = self.applicant.username + '-' + self.quiz.name
        return title

    def percentage(self):
        per = self.obtained*100/self.total
        return per