from django.urls import path
from . import views


app_name = 'attendances'


urlpatterns=[
    path('',views.index,name='index'),
    path('/<int:pk>/', views.attendances, name='attendances'),
    path('/update_attendance',views.update_attendance,name='update_attendance')

]

 



