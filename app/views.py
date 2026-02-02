from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse

# Create your views here.

def landing(req):
    return render(req,'landing.html')


def register(req):
    return render(req,'register.html')

def emp_list(req):
    emp=Employee.objects.all()
    print(emp.values())

    print(emp.values_list())