from django.urls import path
from students.views import StudentViewSet, add_students

urlpatterns = [
    path('', StudentViewSet.as_view(), name='students'),
    # path('enlist/', StudentEnlistmentViewSet.as_view(), name='enlist'),
    path('add/', add_students, name='add'),
]
