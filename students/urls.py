from django.urls import path
from students.views import StudentViewSet, add_students, add_courses

urlpatterns = [
    path('', StudentViewSet.as_view(), name='students'),
    path('add_students/', add_students, name='add'),
    path('add_courses/', add_courses, name='add'),
]
