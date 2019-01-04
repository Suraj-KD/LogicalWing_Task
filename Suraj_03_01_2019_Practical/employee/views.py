from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.models import Employee
from employee.serializers import EmployeeSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def employee_list(request, format=None):
    """
      List all code snippets, or create new snippet.
    """
    if request.method == 'GET':
        snippet = Employee.objects.all()
        serializer = EmployeeSerializer(snippet, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk, format=None):
    """
      Retrieve, update and delete code snippet.
    """
    try:
       snippet = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = EmployeeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
