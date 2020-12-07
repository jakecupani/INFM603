from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Question, Choice


# Create your views here.
def quiz(request):
    # get all the quizzes
    # filter by selected difficulty
    context = {}
    questions = Question.objects.all()
    context['topics'] = ["Other","Artemis"]
    context['questions'] = questions
    print(questions)
    return render(request,"quiz.html",context)