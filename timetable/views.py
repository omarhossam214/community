from django.shortcuts import render,get_object_or_404
from django.core import serializers

from timetable.models import Classes,periods
from team.models import Staff
import json 
from django.http import JsonResponse
from active.models import ActiveCourse,instructor,Attendance
# Create your views here.

import datetime
import pandas as pd
from team.models import Staff,Student
from courses.models import Course

from dateutil import parser

from datetime import timedelta
from django.forms.models import model_to_dict
from.models import periods
import json
from collections import OrderedDict
from django.http import HttpResponse
from active.models import ActiveCourse,AttendanceRecord
from collections import defaultdict




def index(request):

    # Retrieve all instances of the instructor model
    instructors = instructor.objects.all()

    
    for instructor_instance in instructors:
        print(instructor_instance.get_active_course_period)


    return render(request, 'timetable/timetable.html', {'instructors': instructors})







def attendances(request, pk):
    active = get_object_or_404(ActiveCourse, pk=pk)
    
    # Check if the ActiveCourse object exists Attendance
    if active:
        # Get the course_classes_count for the ActiveCourse
        students_classes_count = Attendance.objects.filter(active_course=active).first()

        
        classes_count = students_classes_count.get_course_classes_count


        classes = [f'Class {i}' for i in range(1, classes_count + 1)]

        attendance_records = students_classes_count.get_AttendanceRecord

        print(classes)
        


        return render(request, 'attendace/attendace.html',{'attendance_records':attendance_records,'classes':classes})