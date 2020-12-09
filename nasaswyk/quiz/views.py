from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Question, Choice, Quiz


# Create your views here.
def quiz(request):
    # get all the quizzes
    # filter by selected difficulty
    context = {}
    quizzes = Quiz.objects.all()
    context['topics'] = ["Other","Artemis"]
    context['quizzes'] = quizzes
    
    return render(request,"quiz.html",context)

def quiz_questions(request,question_id):
    context = {}
    try:
        quiz = Quiz.objects.filter(pk=question_id)
        quiz = q[0]
    except:
        print('404')
    context['quiz'] = quiz
    return render(request,'quiz_questions.html',context)