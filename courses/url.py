from django.urls import path
from . import views


app_name = 'course'


urlpatterns=[
    path('',views.index,name='index'),
    path('/<int:pk>/', views.coursedetails, name='coursedetails'),
    path('/<int:pk>/submit_form', views.submit_form, name='submit_form'),
]

