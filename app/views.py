from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse,JsonResponse
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def landing(req):
    return render(req,'landing.html')


def register(req):
    return render(req,'register.html')

# (not use serializer , complex data convert to python data) # use core logic

@csrf_exempt
def emp_list(req):
    if req.method=="POST":
        j_data=req.body
        print(j_data)
        print(type(j_data))
        p_data=json.loads(j_data)
        print(p_data)
        print(type(p_data))
        n=p_data.get('name')
        a=p_data.get('age')
        c=p_data.get('city')
        if 'name' in p_data and 'age' in p_data and 'city' in p_data:
            Employee.objects.create(name=n,age=a,city=c)
            d={
                'msg':'object created succesfully'
            }
            j_data=json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')



        




    # emp=Employee.objects.all()
    # print(emp.values())
    # p_emp_data=list(emp.values())
    # print(p_emp_data)
    # j_data=json.dumps(p_emp_data)
    # print(j_data)
    # return HttpResponse(j_data,content_type='application/json')

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




