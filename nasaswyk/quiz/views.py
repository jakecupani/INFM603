from django.shortcuts import render
from django.http import HttpResponse
from quiz.models import Question, Choice, Quiz


# Create your views here.
def quiz(request):
    # get all the quizzes
    # filter by selected difficulty
    context = {}
    def filter_topics(q_set,res):
        print(res['Topic'])
        if res['Topic'] == "Any":
            return Quiz.objects.all()
        q_set = q_set.filter(topic=res['Topic'])
        return q_set

    def filter_difficulty(q_set,res):
        print(res['Difficulty'])
        if res['Difficulty'] == "Any":
            return Quiz.objects.all()
        q_set = q_set.filter(difficulty=res['Difficulty'])
        return q_set

    
    quizzes = Quiz.objects.all()
    res = request.POST

    if res:
        try:
            quizzes = filter_topics(quizzes,res)
        except:
            pass
        try:
            quizzes = filter_difficulty(quizzes,res)
        except:
            pass
    
    context['topics'] = ["Other","Missions","Spacecraft","Spacesuits","Spaceships","NASA Names"]
    context['quizzes'] = quizzes

    print(res)
    return render(request,"quiz.html",context)

def quiz_questions(request,quiz_id):
    context = {}
    res = request.POST
    context['message'] = False
    def checkAnswers(res):
        print(res)
        score = 0
        total_questions = 0
        incorrect = []

        for i in res:
            if i == "csrfmiddlewaretoken":
                continue
            elif res[i] == "True":
                score += 1
                total_questions += 1
            else:
                incorrect.append(Question.objects.get(title=i))
                total_questions += 1
        
        context['incorrect'] = incorrect

        if total_questions == 0:
            return 0
        else:
            return int((score/total_questions)*100)

    if res:
        context['message'] = True
        context['score'] = checkAnswers(res)
    try:
        quiz = Quiz.objects.filter(pk=quiz_id)
        quiz = quiz[0]

        questions = Question.objects.filter(quiz=quiz)
    except:
        print('404')
    context['quiz'] = quiz
    context['questions'] = questions
    print(context)
    return render(request,'quiz_questions.html',context)