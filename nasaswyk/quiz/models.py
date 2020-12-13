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
        ("Missions",'Missions'),
        ("Spacecraft","Spacecraft"),
        ("Spacesuits","Spacesuits"),
        ("Spaceships","Spaceships"),
        ("NASA Names","NASA Names"),
    ]


class Quiz(models.Model):

    def __str__(self):
        return self.title
    
    title = models.CharField(default='',max_length=1000)
    topic = models.CharField(default='Other',max_length=100,choices=TOPICS)
    difficulty = models.CharField(default='Easy',max_length=100,choices=DIFFICULTIES)
    thumbnail = models.ImageField(default=None)
    description = models.TextField(default='')


class Question(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(default='',max_length=1000)
    description = models.TextField(default="")    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,default=None)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    