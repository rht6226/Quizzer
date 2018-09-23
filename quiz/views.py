from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
from .models import Quiz, Question, Answers
import os, csv
from random import shuffle

def timer(request):
    return render(request,'indexTimer.html')
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
            try:
                qu = Quiz.objects.get(Quiz_id = request.POST['Quiz_id'])
                create_quiz_form = QuizForm()
                return render(request, 'create_quiz.html', {'quiz_form': create_quiz_form, 'error': "Quiz id is already taken! "})
            except Quiz.DoesNotExist:
                item.name = request.POST['name']
                item.csv_file = request.FILES['csv_file']
                item.about = request.POST['about']
                item.Quiz_id=request.POST['Quiz_id']
                item.Test_Password=request.POST['Test_Password']
                item.instructions = request.POST['instructions']
                item.positive = request.POST['positive']
                item.negative = request.POST['negative']
                item.duration = request.POST['duration']
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
                messages.info(request,'Your Quiz has been submitted successfully. Share the credentials and start   quizzing!')
                return redirect( 'dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # get request. We have to return the form so that user can fill it.
        create_quiz_form = QuizForm()
        return render(request, 'create_quiz.html', {'quiz_form': create_quiz_form})

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
    item = get_object_or_404(Quiz, Quiz_id=quizid)
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
                dicty['result'] = '+' + str(item.positive)
                marks = marks + item.positive
            else:
                dicty['result'] = '-' + str(item.negative)
                marks = marks - item.negative
        list_object.append(dicty)
        total_marks = 3* len(list_object)
    return render(request, 'score.html', {'quiz_object': item, 'score': marks, 'data': list_object, 'max': total_marks})


@login_required(login_url = '/accounts/login')
def conduct_quiz(request, quizid):
    aspirant = request.user
    item = get_object_or_404(Quiz, Quiz_id=quizid)
    data = Question.objects.filter(quiz = item)
    if request.method == 'POST':
        ques = get_object_or_404(Question, id=request.POST['question_id'])
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
        
    return render(request, 'quiz1.html', {'quiz_object': item, 'quiz_data': querys})
