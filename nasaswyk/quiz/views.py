from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def quiz(request):
    # get all the quizzes
    # filter by selected difficulty
    context = {}
    return render(request,"quiz.html",context)