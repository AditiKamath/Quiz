from django.shortcuts import get_object_or_404, redirect, render , HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from .models import *
from .forms import *

# Create your views here.
# register user 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registration Successful')
            form.save()
            return HttpResponseRedirect('/login/')
    else :
        form =UserRegistrationForm()
    return render(request, 'custom/register.html',{'form':form})

# Login 
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username = uname, password = upass)
            if user is not None :
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else : 
        form = AuthenticationForm()
    return render(request,'custom/user_login.html',{'form':form})

def user_profile(request):
    return render(request,'custom/user_profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#create quiz
def createQuiz(request):
    if(request.method == 'GET'):
        return render(request,'Quiz/Quiz_name.html') 
    
    if(request.method == 'POST'):
        quiz_name = request.POST['q_name']
        new_quiz = Quiz.objects.create(quizName = quiz_name)
        return HttpResponseRedirect('/addQuestion/' + str(new_quiz.id) + '/')
    

#add question
def addQuestion(request, id):    
    if(request.method == 'GET'):
        quiz = Quiz.objects.get(id=id)
        question = Question.objects.filter(parentQuiz = quiz)
        lst = []
        for i in question:
            option_text = []
            option = Option.objects.filter(parentQuestion = i)
            count = 0
            for j in option:
                count=count+1
                option_text.append(j.text)
                if j.isAns:
                    answer = count
            required = (i.text,option_text,answer)
            lst.append(required)
            #(question,option,answer)
        return render(request,'Quiz/addQuestion.html', {"lst":lst}) 
      



    if(request.method=='POST'):
        question = request.POST['ques']
        op1 = request.POST['op1']
        op2 = request.POST['op2']
        op3 = request.POST['op3']
        op4 = request.POST['op4']
        ans = request.POST['ans']
        quiz = Quiz.objects.get(id=id)
        question = Question.objects.create(parentQuiz = quiz,text = question)
        lst = [op1,op2,op3,op4]
        count = 0
        for i in lst:
            count = count+1
            if i=="":
                continue
            else:
                if int(count)==int(ans):
                    Option.objects.create(parentQuestion=question,text=i,isAns=True)
                else:
                    Option.objects.create(parentQuestion=question,text=i,isAns=False)
        return HttpResponseRedirect('/addQuestion/' + str(id) + '/')
    

#*************************************Quiz Endpoints****************************#
def getQuiz(request, quizId) :   

    if(request.method == "POST"):
        #Getting the quiz
        quiz = get_object_or_404(Quiz, pk=quizId)
        
        #Calculating the score
        score = 0
        for key,value in request.POST.items() :
            if(key != "csrfmiddlewaretoken") :
                if(quiz.question_set.get(pk=int(key)).option_set.get(pk=int(value)).isAns) :
                    score += 1

        #Compiling the results
        results = []
        for question in quiz.question_set.all() :
            results.append([question.text, question.option_set.get(isAns=True).text, question.option_set.get(pk=request.POST[f"{question.id}"]).text])
            results[-1].append(results[-1][1] == results[-1][2])
        
        return render(request, "Quiz/quizResults.html", {"quiz": quiz, "playerScore": score, "results": results})

    else :
        #Getting the quiz
        quiz = get_object_or_404(Quiz, pk=quizId)

        #Creating the option map
        options = {}
        for question in quiz.question_set.all() :
            options[question.id] = []
            for option in question.option_set.all() :
                options[question.id].append(option)
        
        return render(request, "Quiz/quiz.html", {"quiz": quiz, "questions": quiz.question_set.all(), "options": options})

