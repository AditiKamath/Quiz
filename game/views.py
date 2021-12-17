from django.shortcuts import get_object_or_404, render , HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
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
        new_quiz = NewQuiz.objects.create(quiz_name = quiz_name)
        return HttpResponseRedirect('/addQuestion/' + str(new_quiz.id) + '/')
    

#add question
def addQuestion(request, id):    
    if(request.method == 'GET'):
        quiz_name = NewQuiz.objects.get(id=id)
        question = QuesModel.objects.filter(quiz_name = quiz_name)
        return render(request,'Quiz/addQuestion.html', {"question":question}) 



    if(request.method=='POST'):
        question = request.POST['ques']
        op1 = request.POST['op1']
        op2 = request.POST['op2']
        op3 = request.POST['op3']
        op4 = request.POST['op4']
        ans = request.POST['ans']
        quiz_name = NewQuiz.objects.get(id=id)
        ques_model = QuesModel.objects.create(quiz_name = quiz_name, question=question, op1 = op1, op2 = op2, op3 = op3, op4 = op4, ans = ans)

        return HttpResponseRedirect('/addQuestion/' + str(id) + '/')
    

#*************************************Quiz Endpoints****************************#
def getQuiz(request, quizId) :   
    
    #Getting the quiz
    quiz = get_object_or_404(Quiz, pk=quizId)
    
    return render(request, "Quiz/quiz.html", {"quiz": quiz, "questions": quiz.question_set.all()})



