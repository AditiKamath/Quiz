from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Quiz(models.Model) :
    quizName = models.CharField(max_length=100)
    quizScore = models.IntegerField(null=True, blank=True)

class Question(models.Model) :
    parentQuiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

class Option(models.Model) :
    parentQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    isAns = models.BooleanField() 


"""
class NewQuiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.quiz_name


class QuesModel(models.Model):
    quiz_name = models.ForeignKey(NewQuiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    op1 = models.CharField(max_length=100)
    op2 = models.CharField(max_length=100)
    op3 = models.CharField(max_length=100)
    op4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question
"""
