from django.shortcuts import get_object_or_404, render , HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from .models import Quiz

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

#*************************************Quiz Endpoints****************************#
def getQuiz(request, quizId) :   
    
    #Getting the quiz
    quiz = get_object_or_404(Quiz, pk=quizId)
    
    return render(request, "Quiz/quiz.html", {"quiz": quiz, "questions": quiz.question_set.all()})
