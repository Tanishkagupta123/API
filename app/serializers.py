def employee_serializer(emp):
    return {
        'id': emp.id,
        'name': emp.name,
        'age': emp.age
    }
