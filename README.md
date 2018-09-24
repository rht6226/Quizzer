# Quizzer

## Introduction
Created a quizzing platform to be used in conducting online quizzes using DJANGO. The platform uses different Django apps to provide functionalities like User creation / authentication, Creating New Quizzes using CSV files, Conducting Quizzes and producing the overall score.

## Scope
This Project can be utilized in a wide range of Educational Institutes like Colleges, Schools, Coaching Institutes etc. It is still under development and I plan on keep working on it till it is ready to be used commercially.
## Instructions to run locally
1.Install Python and some dev tools for Python
  -$ sudo apt-get install python-pip python-dev build-essential
  -$ apt install Python3.6
2. use easy_install for older versions of ubuntu e.g -$ easy_install python3-pip
3. Install Pip
   -$ apt install python3-pip
4. Install other requirements given in requirements.txt file`
   -$ pip install requirements.txt
5. Modify database engine,
   -Comment line 100-114 in settings.py
   -uncomment line 115-120
   save changes
6. sync db
   -$ python manage.py makemigrations
   -$ python manage.py migrate
7.runserver
  -$ Python manage.py runserver
  -$ visit 127.0.0.1:8000
8. Done :-)

