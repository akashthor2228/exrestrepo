from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student

class StudentAPI(APIView):

    def get(self,request):
        all_students = Student.objects.all()

        student_list = []
        for s in all_students:
            student_dict = {
                "name" : s.name,
                "age" : s.age,
            }
            student_list.append(student_dict)

        return Response(student_list)

    def post(self,request):
        print(request.data)

        new_student = Student(name = request.data['name'],age = request.data['age'])
        new_student.save()

        return Response("api")


def index(request):
    students = Student.objects.all().values_list('name')
    return render(request,'index.html',{"students":students})