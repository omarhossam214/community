from django.urls import path
from . import views


app_name='schedule'


urlpatterns=[
    path('',views.index,name='index'),
    path('/process_schedule',views.process_schedule,name='schedule'),
]

 