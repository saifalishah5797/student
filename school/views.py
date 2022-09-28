from django.shortcuts import render

# Create your views here.
from .models  import Student

def home(request):
    student_data = Student.objects.all()
    print("return:", student_data)
    print()
    print("SQL query:", student_data.query)

    return render(request, 'school/home.html' , {'students': student_data})