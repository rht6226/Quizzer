from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from .models import Quiz, Question, Answers
import os, csv
from random import shuffle

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
    print(data)
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
            item.quiz_id = request.POST['quiz_id']
            item.quiz_password = request.POST['quiz_password']
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
            return redirect('/quiz/test/edit/'+ item.quiz_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # get request. We have to return the form so that user can fill it.
        create_quiz_form = QuizForm()
        return render(request, 'createquiz.html', {'quiz_form': create_quiz_form})

def create_answer_table(quiz_object, question_objects, user_object):
    for question_object in question_objects:
        ans = Answers()
        ans.applicant = user_object
        ans.quiz = quiz_object
        ans.question = question_object
        ans.correct_choice = question_object.correct
        ans.save()
    return

@login_required(login_url = '/accounts/login')
def score(request, quizid):
    aspirant = request.user
    item = get_object_or_404(Quiz, quiz_id=quizid)
    answers = Answers.objects.filter(quiz = item, applicant=aspirant)
    list_object = []
    marks = 0
    for answer in answers:
        dicty = dict()
        ques = answer.question
        dicty['question'] = ques.question
        dicty['submission'] = answer.response
        dicty['correct'] = answer.correct_choice
        if answer.response == '':
            marks = marks
            dicty['result'] = '0'
        else:
            if answer.response == answer.correct_choice:
                dicty['result'] = '+3'
                marks = marks + 3
            else:
                dicty['result'] = '-1'
                marks = marks - 1
        list_object.append(dicty)
        total_marks = 3* len(list_object)
    return render(request, 'score.html', {'quiz_object': item, 'score': marks, 'data': list_object, 'max': total_marks})

@login_required(login_url = '/accounts/login')
def conduct_quiz(request, quizid):
    aspirant = request.user
    item = get_object_or_404(Quiz, quiz_id=quizid)
    data = Question.objects.filter(quiz = item)
    if request.method == 'POST':
        ques = get_object_or_404(Question, id=request.POST.get('question_id'))
        answer_object = get_object_or_404(Answers, applicant=aspirant, quiz=item, question=ques)
        answer_object.response = request.POST.get('response')
        answer_object.save()
    
    querys = []
    for thing in data:
        querys.append(thing)

    else:
        try:
            answers = get_list_or_404(Answers, applicant=aspirant, quiz=item)
        except:
            create_answer_table(item, data, aspirant)
    shuffle(querys)
        
    return render(request, 'takequiz.html', {'quiz_object': item, 'quiz_data': querys})

@login_required(login_url = '/accounts/login')
def welcome(request, quizid):
    item = get_object_or_404(Quiz, quiz_id=quizid)
    return render(request, 'quizfront.html', {'quiz_object': item})

@login_required(login_url = '/accounts/login')
def edit_quiz(request, quizid):
    aspirant = request.user
    item = get_object_or_404(Quiz, quiz_id=quizid)
    data = Question.objects.filter(quiz = item)
    if request.method == 'POST':
        ques = get_object_or_404(Question, id=request.POST.get('question_id'))
        ques.image = request.POST.get('img')
        ques.code = request.POST.get('code')
        ques.save()
    querys = []
    for thing in data:
        querys.append(thing)        
    return render(request, 'editquiz.html', {'quiz_object': item, 'quiz_data': querys})
        