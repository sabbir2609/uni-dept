from django.views.generic import ListView

from students.models import User


class StudentViewSet(ListView):
    model = User
    template_name = "students/index.html"
    context_object_name = "students"
