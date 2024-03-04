from django.urls import path
from . import views


app_name = 'attendances'


urlpatterns=[
    path('',views.index,name='index'),
    path('/<int:pk>/', views.attendances, name='attendances'),
]

 



