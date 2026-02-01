from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from .serializers import employee_serializer

@csrf_exempt
def list(request):

    if request.method == 'GET':
        employees = Employee.objects.all()
        data = []

        for emp in employees:
            data.append(employee_serializer(emp))

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        emp = Employee.objects.create(
            name=body['name'],
            age=body['age']
        )
        return JsonResponse(employee_serializer(emp))
