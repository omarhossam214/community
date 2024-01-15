from django.shortcuts import render,get_object_or_404
from .models import Course
from timetable.models import periods
import json
from active.models import ActiveCourse
# Create your views here.

from django.http import JsonResponse
from team.models import instructor
from active.models import pupl

from django.core.mail import send_mail
from django.conf import settings

import time




def index(request):

    courses = Course.objects.all()

    return render(request,'courses/courses.html',{'courses':courses})



def coursedetails(request, pk):

    course = get_object_or_404(Course, pk=pk)

    Periods = periods.objects.all()  

    return render(request, 'course-detail/course-detail.html', {'course': course, 'periods': Periods})



def submit_form(request, pk):
    # Record the start time
    start_time = time.time()

    # Retrieve the Course object based on the provided primary key (pk)
    course = get_object_or_404(Course, pk=pk)

    # Parse JSON data from the request body
    data = json.loads(request.body)

    # Extract data from the JSON payload
    name = data['form']['Name']
    phone = data['form']['Phone']
    email = data['form']['Email']
    start_date = data['form']['startDate']
    shift = data['form']['shift']

    # Get an instructor with the least number of active courses
    instructor_id_with_less_count = instructor.get_instructor_with_less_count()

    # Get or create an ActiveCourse instance for the given course and instructor
    activecourse, created_1 = ActiveCourse.objects.get_or_create(
        course=course,
        teacher=instructor_id_with_less_count,
        start_date = start_date,
    )

    # Get or create an ActiveStudent instance for the given activecourse, phone, name, and email
    activestudent, created_2 = pupl.objects.get_or_create(
        active=activecourse,
        phone=phone,
        name=name,
        email=email,
    )

    # If a new ActiveStudent instance is created, update the enrolled count in ActiveCourse
    if created_2:
        activecourse.enrolled = activecourse.enrolled + 1
        activecourse.save()


    # Record the end time
    end_time = time.time()

    # Calculate and print the runtime
    runtime = end_time - start_time
    print(f"Runtime: {runtime} seconds")
    print(shift)


    # Return the JsonResponse or other response as needed
    return JsonResponse({'message': 'The student is already enrolled'})
   


