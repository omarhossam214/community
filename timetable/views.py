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
    
    # Check if the ActiveCourse object exists
    if active:
        # Get the course_classes_count for the ActiveCourse
        students_classes_count = Attendance.objects.filter(active_course=active).first().get_course_classes_count

        # Retrieve all AttendanceRecord instances based on active_course_id
        attendance_records = AttendanceRecord.objects.filter(attendance__active_course=active)

        # Generate a list of class names
        classes = [f'Class {i}' for i in range(1, students_classes_count + 1)]

        # Create a dictionary to store organized data
        student_data = defaultdict(lambda: {'student': None, 'classes': []})

        for record in attendance_records:
            student_name = record.student.name  # Assuming 'name' is the field for student name
            attended_status = record.attended

            # Update the dictionary
            student_data[student_name]['student'] = student_name
            student_data[student_name]['classes'].append({'attended': attended_status})

        # Convert the dictionary values to a list for rendering
        organized_data = list(student_data.values())


        print(student_data)

        return render(request, 'attendace/attendace.html', {'classes': classes, 'organized_data': organized_data})