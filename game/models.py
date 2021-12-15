from django.db import models

# Create your models here.
class Quiz(models.Model) :
    quizName = models.CharField(max_length=100)
    quizScore = models.IntegerField()

class Question(models.Model) :
    parentQuiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

class Option(models.Model) :
    parentQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    isAns = models.BooleanField() 