from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def landing(req):
    return render(req, 'landing.html')


def register(req):
    return render(req, 'register.html')

# (not use serializer , complex data convert to python data) # use core logic

@csrf_exempt
def emp_list(req):
    if req.method =="POST":
        j_data = req.body
        print(j_data)
        print(type(j_data))
        p_data= json.loads(j_data)
        print(p_data)
        print(type(p_data))
        n= p_data.get('name')
        a= p_data.get('age')
        c= p_data.get('city')
        if 'name' in p_data and 'age' in p_data and 'city' in p_data:
            Employee.objects.create(name=n,age=a,city=c)
            d = {
                'msg': 'Object created successfully'
            }
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
        else:
            d = {
                'msg': 'Some required field values are not found'
            }
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
    emp = Employee.objects.all()
    # print(emp.values())
    p_emp_data = list(emp.values())
    # print(p_emp_data)
    j_data= json.dumps(p_emp_data)
    # print(j_data)
    return HttpResponse(j_data,content_type='application/json')

    # return JsonResponse(p_emp_data,safe=False)

@csrf_exempt
def details(req,pk):
    if req.method =="PUT":
        j_data = req.body
        print(j_data)
        print(type(j_data))
        p_data= json.loads(j_data)
        print(p_data)
        print(type(p_data))
        if 'name' in p_data and 'age' in p_data and 'city' in p_data:
            old_data = Employee.objects.get(id=pk)
            old_data.name = p_data.get('name')
            old_data.age = p_data.get('age')
            old_data.city = p_data.get('city')
            old_data.save()
            d = {
                'msg': 'Object updated successfully'
            }
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
        else:
            d = {
                'msg': 'All fields are required'
            }
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
    
    elif req.method =="PATCH":
        j_data = req.body
        print(j_data)
        print(type(j_data))
        p_data= json.loads(j_data)
        print(p_data)
        print(type(p_data))
        old_data = Employee.objects.get(id=pk)
        if 'name' in p_data:
            old_data.name = p_data.get('name')
        if 'age' in p_data:
            old_data.age = p_data.get('age')
        if 'city' in p_data:
            old_data.city = p_data.get('city')
        old_data.save()
        d = {
                'msg': 'Object partially updated successfully'
            }
        j_data = json.dumps(d)
        return HttpResponse(j_data,content_type='application/json')
    
    elif req.method =="DELETE":
        old_data = Employee.objects.get(id=pk)
        old_data.delete()
        d = {
                'msg': 'Object Deleted successfully'
            }
        j_data = json.dumps(d)
        return HttpResponse(j_data,content_type='application/json')
    
    emp = Employee.objects.get(id=pk)
    print(emp)
    p_data = model_to_dict(emp)
    # print(p_data)
    # j_data= json.dumps(p_data)
    # print(j_data)
    # return HttpResponse(j_data,content_type='application/json')
    return JsonResponse(p_data,safe=False)



@csrf_exempt
def employee(req):
    j_data =req.body
    if j_data:
        p_data=json.loads(j_data)

        if 'id' in p_data:
            id_in_db = Employee.objects.filter(id = p_data.get('id'))
            if id_in_db:
                if req.method =="PUT":
                    if 'name' in p_data and 'age' in p_data and 'city' in p_data:
                        old_data = Employee.objects.get(id=p_data.get('id'))
                        old_data.name = p_data.get('name')
                        old_data.age = p_data.get('age')
                        old_data.city = p_data.get('city')
                        old_data.save()
                        d = {
                            'msg': 'Object updated successfully'
                        }
                        j_data = json.dumps(d)
                        return HttpResponse(j_data,content_type='application/json')
                    else:
                        d = {
                            'msg': 'All fields are required'
                        }
                        j_data = json.dumps(d)
                        return HttpResponse(j_data,content_type='application/json')
                
                elif req.method == "PATCH":
                    old_data = Employee.objects.get(id=p_data.get('id'))
                    if 'name' in p_data:
                        old_data.name = p_data.get('name')
                    if 'age' in p_data:
                        old_data.age = p_data.get('age')
                    if 'city' in p_data:
                        old_data.city = p_data.get('city')
                    old_data.save()
                    d = {
                            'msg': 'Object partially updated successfully'
                        }
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')

                elif req.method == "DELETE":
                    old_data = Employee.objects.get(id=p_data.get('id'))
                    old_data.delete()
                    d = {
                            'msg': 'Object Deleted successfully'
                        }
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
                
                emp_data = Employee.objects.get(id=p_data.get('id'))
                p_data = model_to_dict(emp_data)
                print(p_data)
                j_data= json.dumps(p_data)
                print(j_data)
                return HttpResponse(j_data,content_type='application/json')
                # return JsonResponse(p_data,safe=False)
            else:
                d = {
                            'msg': 'Id not present in DB'
                        }
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')

        else:
            if req.method =="POST":
                n= p_data.get('name')
                a= p_data.get('age')
                c= p_data.get('city')
                if 'name' in p_data and 'age' in p_data and 'city' in p_data:
                    Employee.objects.create(name=n,age=a,city=c)
                    d = {
                        'msg': 'Object created successfully'
                    }
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
                else:
                    d = {
                        'msg': 'Some required field values are not found'
                    }
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
            emp = Employee.objects.all()
            # print(emp.values())
            p_emp_data = list(emp.values())
            # print(p_emp_data)
            j_data= json.dumps(p_emp_data)
            # print(j_data)
            return HttpResponse(j_data,content_type='application/json')

    else:
        emp = Employee.objects.all()
        # print(emp.values())
        p_emp_data = list(emp.values())
        # print(p_emp_data)
        j_data= json.dumps(p_emp_data)
        # print(j_data)
        return HttpResponse(j_data,content_type='application/json')
    
    # Used to Serializer----------------------------
    
from .serializers import EmpSerializer  
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

@csrf_exempt
def seralizeall(req):
    if req.method=="POST":
        data=req.body  
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        serializer = EmpSerializer(data=p_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()  
            d = {
                'msg': 'Object created successfully'
            }
            j_data = JSONRenderer().render(d)
            return HttpResponse(j_data,content_type='application/json')
    
        else:
          j_data = JSONRenderer().render(serializer.errors)
          return HttpResponse(j_data,content_type='application/json')
    

    data = Employee.objects.all()
    serializer =  EmpSerializer(data,many=True)
    print(serializer)
    print(serializer.data)

    # Old method----------------
    # j_data= json.dumps(serializer.data)
    #     # print(j_data)
    # return HttpResponse(j_data,content_type='application/json')

    # new ------------
    # json = JSONRenderer().render(serializer.data)
    # return HttpResponse(json,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def seralizeone(req,pk):
    if req.method == 'PUT':
        data = req.body
        stream = io.BytesIO(data)
        new_p_data = JSONParser().parse(stream)
        old_emp = Employee.objects.get(id=pk)

        serializer = EmpSerializer(old_emp, data=new_p_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Object updated successfully'})
        else:
            return JsonResponse(serializer.errors)
    
    if req.method == 'PATCH':
        data = req.body
        stream = io.BytesIO(data)
        new_p_data = JSONParser().parse(stream)
        old_emp = Employee.objects.get(id=pk)

        serializer = EmpSerializer(old_emp, data=new_p_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Object updated successfully'})
        else:
            return JsonResponse(serializer.errors)
    
    if req.method == 'DELETE':
        emp = Employee.objects.get(id=pk)
        emp.delete()
        return JsonResponse({'msg': 'Object deleted successfully'}) 

    data = Employee.objects.get(id=pk)
    serializer =  EmpSerializer(data)
    # json = JSONRenderer().render(serializer.data)
    # return HttpResponse(json,content_type='application/json')
    return JsonResponse(serializer.data)


