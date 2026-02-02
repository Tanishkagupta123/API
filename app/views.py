from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse,JsonResponse
import json
from django.forms.models import model_to_dict

# Create your views here.

def landing(req):
    return render(req,'landing.html')


def register(req):
    return render(req,'register.html')

def emp_list(req):
    emp=Employee.objects.all()
    print(emp.values())
    p_emp_data=list(emp.values())
    print(p_emp_data)
    j_data=json.dumps(p_emp_data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')

    # return JsonResponse(p_emp_data,safe=False)

def details(req,pk):
    emp=Employee.objects.get(id=pk)
    print(emp)
    p_data = model_to_dict(emp)
    # print(p_data)
    # j_data=json.dumps(p_data)
    # print(j_data)
    # return HttpResponse(j_data,content_type='application/json')
    return JsonResponse(p_data,safe=False)



