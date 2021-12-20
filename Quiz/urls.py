"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path("quizlist/", views.quizList, name="quizList"),
    path("quiz/<int:quizId>", views.getQuiz, name="getQuiz"),
    # path('profile/createQuiz/', views.createQuiz,name='createQuiz'),
    # path('addQuestion/<int:id>/', views.addQuestion,name='addQuestion'),
    #path('createQuiz/', views.createQuiz,name='createQuiz'),
    #path('addQuestion/<int:id>/', views.addQuestion,name='addQuestion'),
]
