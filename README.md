# Quizzer

## Introduction

Most of us don't generally test ourselves as much as we would like to do. There is uncertainity in not knowing. We tell ourselves when the moment arrives we will take everything seriously and ace the test.
This is a very common problm among students. There is either a lack of available platforms or the market is filled with online platform that claim to be up to the mark.
We tried to solve a common problem most of us face. When we were looking at all the problem statements of INNODEV 2018 the one called *Ample samples* intrigued us the most. The Idea of actually creating a platform for conducting professional level quizzes was very interesting.

## Problem statement - **Ample Samples**

*The placements sessions are here and an overconfident Apurva thinks she is a know it all. Her friends want to help her but couldn’t as she doesn't like their preaching. So her friends thought of challenging her in a quiz related to their subject to break her overconfidence. The only problem is that they don't have a platform where they can conduct such quizzes. Help the friends design a quiz platform which can be easily used to conduct quizzes and their easy evaluation. Also her friends want the solution to be user friendly as Apurva wouldn't take the quiz if she faces any trouble in handling the platform. Use your imagination to help Apurva in taking the placement sessions seriously.*

All of us face these kind of problems. In most of the colleges or schools there is a lack of a local platform fo testing our skills. We tried to solve this problem in this project.

Our aim was to make the experience of quizzing as smooth as possible. From registration, login to creating and participating in quizzes. We tried to think of the problems faced by both the quiz-administrators and the students and then tried to solve them as much as was possible in the given amount of time.

## Technologies and Tools

1. **Language** - Python 3.6
2. **Backend Framework** - Django 2.1
3. **Database** - POSTGRESQL
4. **DBMS** - Pgadmin 
5. **Version-control** - Git and Github
6. **JavaScript Library** - jquery (primarily used for AJAX)
7. **Style Libraries** - Bootstrap

## Scope

This Project can be utilized in a wide range of Educational Institutes like Colleges, Schools, Coaching Institutes etc. It is still under development and we plan to keep working on it till it is ready to be used commercially.Hopefully if it turns out to be good enough we will be able to support all the online quizzes held in our college at the local level.

The room for development is enourmous. We can first start by adding a code editor and an online judge. We can use webscraping to scrape the best quizzes from the net. ML can be implemented to predict quiz chices for students who are here to practice. Quiz-groups features can be added and some imitation of hackerearth's code arena can also be added. 

The main reason behind choosing this project was that we can keep on working on it and improving it.

## Instructions to run locally
1. Install Python and some dev tools for Python
 - $ sudo apt-get install python-pip python-dev build-essential
 - $ apt install Python3.6
 - use easy_install for older versions of ubuntu e.g -$ easy_install python3-pip
2. Install Pip
 - $ apt install python3-pip
3. Install other requirements given in requirements.txt file
 - $ pip install requirements.txt
4. Modify database engine,
 - Rename the database section in settings.py 
 - add username and password and port accordingly
 - save changes
5. Sync db and make superuser
 - $ python manage.py makemigrations
 - $ python manage.py migrate
 - $ python manage.py createsuperuser
6. Collect Static files
 - python manage.py collectstatic
6. Runserver
 - $ Python manage.py runserver
 - $ visit 127.0.0.1:8000
7. Done :-)
