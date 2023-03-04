from django.views.generic import ListView, TemplateView

from django.shortcuts import render

from students.models import User


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

        print( name, address, nid,phone, birthdate,gender)

    return render(request, "students/add_students.html")