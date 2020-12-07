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

def question(request,question_id):
    context = {}
    try:
        q = Question.objects.filter(pk=question_id)
        q = q[0]
    except:
        print('404')
    context['question'] = q
    return render(request,'question.html',context)