from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from .models import Quiz, Question
import os, csv

# Create your views here.
def home(request):
    return render(request, 'index.html')

def clean(f):
    data = list()
    with open(f, 'r') as file:
        text = file.read()
    list1 = text.split('\n')
    list1 = list1[1:]
    for item in list1:
        list2 = item.split(',')
        data.append(list2)
    return data

@login_required(login_url = '/accounts/login')
def create(request):
    if request.method == 'POST':
        # form is submitted
        quiz_form = QuizForm(request.POST, request.FILES, request.user)
        if quiz_form.is_valid:
            item = Quiz()
            item.name = request.POST['name']
            item.csv_file = request.FILES['csv_file']
            item.about = request.POST['about']
            item.quizmaster = request.user
            item.save()
            url = item.csv_file.url
            l = url.split('/')
            s = "\\"
            s = s.join(l)
            f = os.getcwd() + s
            data = clean(f)
            for row in data:
                ques = Question()
                ques.quiz = item
                ques.question = row[0]
                ques.a = row[1]
                ques.b = row[2]
                ques.c = row[3]
                ques.d = row[4]
                ques.correct = row[5]
                ques.save()
            messages.success(request, 'Quiz Successfully created! ')
            return redirect('/quiz/test/'+ str(item.id))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # get request. We have to return the form so that user can fill it.
        create_quiz_form = QuizForm()
        return render(request, 'createquiz.html', {'quiz_form': create_quiz_form})


@login_required(login_url = '/accounts/login')
def conduct_quiz(request, quiz_id):
    item = get_object_or_404(Quiz, pk=quiz_id)
    data = item.questions
    return render(request, 'takequiz.html', {'quiz_object': item, 'quiz_data': data})




        