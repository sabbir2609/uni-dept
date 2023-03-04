from django.urls import path
from students.views import StudentViewSet

urlpatterns = [
    path('', StudentViewSet.as_view(), name='students'),
]
