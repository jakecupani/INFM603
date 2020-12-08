from django.db import models
from django.utils import timezone
import datetime

DIFFICULTIES = [
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard')
    ]

TOPICS = [
        ("Other","Other"),
        ("Artemis",'Artemis'),
    ]


# class Quiz(models.Model):

#     def __str__(self):
#         return self.quiz_title
    
#     quiz

class Question(models.Model):
    def __str__(self):
        return self.question_title


    

    question_title = models.CharField(default='',max_length=1000)
    question_description = models.TextField(default="")
    question_reading = models.TextField(default="")
    question_topic = models.CharField(default="Other",choices=TOPICS,max_length=100)
    question_difficulty = models.CharField(default="Easy",choices=DIFFICULTIES,max_length=100)


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    