from django.urls import path
from . import views




urlpatterns=[
    path('',views.index,name='index'),
    path('/get_student_answers',views.get_student_answers,name='get_student_answers')
]

