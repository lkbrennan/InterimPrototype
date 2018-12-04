from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:student_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:student_id>/school/', views.results, name='results'),

    path('parent/signUp/', views.parentSignUp, name='parentSignUp'),
    path('teacher/signUp/', views.teacherSignUp, name='teacherSignUp'),
    path('login', LoginView.as_view(template_name= 'proto/login.html'),name='login'),
    path('',views.home, name='home')
]