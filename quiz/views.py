from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from .models import Quiz, Question
import os, csv


def home(request):
    if request.user.is_authenticated:
        return redirect('accounts/dashboard')
    else:
        return render(request, 'index.html')

@login_required(login_url = '/accounts/login')
def start(request):
    return render(request, 'start.html')


def start_quiz(request):

    if request.method == 'POST':
        try:
           item=Quiz.objects.get(Quiz_id=request.POST['quizid'])

           # item=Quiz(Quiz_id=request.POST['quizid'],Test_password=request.POST['tPass'])

           if item.Test_Password==request.POST['password']:
             request.session['username'] = request.user.get_username()
             return redirect('test/'+str(item.Quiz_id))
           else:

            # return render(request, 'start', {'error': 'Invalid Credentials!'})
            messages.info(request,'Invalid Credentials')
            return redirect('dashboard')
        except Quiz.DoesNotExist:
            messages.info(request,'Quiz does not exists!')
            return redirect('dashboard')
        else:
            return render(request, 'start')

@login_required(login_url = '/accounts/login')
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
            item.Quiz_id=request.POST['Quiz_id']
            item.Test_Password=request.POST['Test_Password']
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
            # messages.success(request, 'Quiz Successfully created! ')
            # return redirect('/quiz/test/'+ str(item.id))
            messages.info(request,'Your Quiz has been submitted successfully. Share the credentials and start quizzing!')
            return redirect( 'dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # get request. We have to return the form so that user can fill it.
        create_quiz_form = QuizForm()
        return render(request, 'create_quiz.html', {'quiz_form': create_quiz_form})


@login_required(login_url = '/accounts/login')
def conduct_quiz(request, quiz_id):
  if 'username' in request.session:
    item = get_object_or_404(Quiz, Quiz_id=quiz_id)
    data = Question.objects.filter(quiz=item)

    querys=[]
    for thing in data:
        querys.append(thing)
    return render(request, 'takequiz.html', {'quiz_object': item, 'quiz_data': querys})
