from django.shortcuts import render,get_object_or_404
from .models import Course
from timetable.models import periods
from django.http import HttpResponse
import json
from team.models import Student
from active.models import ActiveCourse
# Create your views here.

from django.http import JsonResponse
from team.models import Staff,Student,instructor
from active.models import pupl

from django.core.mail import send_mail
from django.conf import settings

import os

from django.db import models



def index(request):

    courses = Course.objects.all()

    return render(request,'courses/courses.html',{'courses':courses})



def coursedetails(request, pk):

    course = get_object_or_404(Course, pk=pk)
    # Change 'periods' to 'Period' or the name of the model you are using
    Periods = periods.objects.all()  # Make sure to use the correct model name

    instructor_id_with_less_count = instructor.get_instructor_with_less_count()

    print(instructor_id_with_less_count)
    print(23232323232323)
    return render(request, 'course-detail/course-detail.html', {'course': course, 'periods': Periods})






def submit_form(request, pk):


    course = get_object_or_404(Course, pk=pk)

    data = json.loads(request.body)


    name =  data['form']['Name']
    Phone =  data['form']['Phone']
    Email =  data['form']['Email']
    periodss =  data['form']['periods']
    startDate =  data['form']['startDate']
    instructor_id_with_less_count = instructor.get_instructor_with_less_count()




    try:
        activecourse, created_1 = ActiveCourse.objects.get_or_create(course = course,teacher=instructor_id_with_less_count)
    except:
         print("can't create activecourse ")

    if not created_1 and activecourse.enrolled < activecourse.capacity:
            ActiveCourse.objects.filter(pk=activecourse.pk)

    elif not created_1 and activecourse.enrolled >= activecourse.capacity:
          activecourse = ActiveCourse.objects.create(course=course,start_date=startDate)


        
    activestudent,  created_2 = pupl.objects.get_or_create(active = activecourse,
                                                               phone = Phone,
                                                               name = name,
                                                               email = Email,
                                                               )



    if created_2 :
 
         activecourse.enrolled = activecourse.enrolled + 1
         activecourse.save()

   

         date = str(
              periods.objects.filter(pk=periodss[0]).first().get_future_date()) + ' ' + str(
                   periods.objects.filter(pk=periodss[0]).first())



    existing_pupil = Student.objects.filter(phone=Phone).first()

    if existing_pupil:

        return JsonResponse({'message': 'the student is already enrolled'})
    
    else:
          
        new_Student = Student(
            name = name,
            phone = Phone,
            email = Email,
        )
        
        new_Student.save()

        return JsonResponse({'message': 'creating a new student'})


   


