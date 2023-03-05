from django.views.generic import ListView, TemplateView

from django.shortcuts import render

from students.models import User, Course


class StudentViewSet(ListView):
    model = User
    template_name = "students/index.html"
    context_object_name = "students"


# class StudentEnlistmentViewSet(TemplateView):
#     template_name = "students/add_students.html"


def add_students(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        nid = request.POST.get("nid")
        phone = request.POST.get("phone")
        birthdate = request.POST.get("birthdate")
        gender = request.POST.get("gender")

        new_student = User(name=name, address=address, nid=nid, phone=phone, birthdate=birthdate, gender=gender)
        new_student.save()

        print(name, address, nid, phone, birthdate, gender)

    return render(request, "students/add_students.html")


def add_courses(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        description = request.POST.get("description")

        new_course = Course(name=name, code=code, description=description)
        new_course.save()

        print(name, code, description)
    return render(request, "students/add_courses.html")
