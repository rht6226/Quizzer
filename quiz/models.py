from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length = 50)
    quiz_id = models.CharField(max_length = 50)
    quiz_password = models.CharField(max_length = 50)
    csv_file = models.FileField(upload_to='quizzes/csv/')
    about = models.TextField(max_length= 2000)
    quizmaster = models.ForeignKey(User, on_delete= models.CASCADE)

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

    def __str__(self):
        title = self.question[:40]
        return title
    

class Answers(models.Model):
    applicant = models.ForeignKey(User, on_delete= models.CASCADE ) 
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    response = models.CharField(max_length=500, default='')
    correct_choice = models.CharField(max_length=500)

