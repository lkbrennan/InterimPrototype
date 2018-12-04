from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Student
from .forms import parentForm

def index(request):
    latest_student_list = Student.objects.all
    context = {'latest_student_list': latest_student_list,}
    return render(request, 'proto/index.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'proto/detail.html', {'student': student})

def results(request, student_id):
    response = "You're looking at the school of student %s."
    return HttpResponse(response % student_id)

def parentSignUp(request):
    return render(request, 'proto/parentSignUp.html')

def home(request):
    return render(request, 'proto/home.html')

def teacherSignUp(request):
    return render(request,'proto/teacherSignUp')
