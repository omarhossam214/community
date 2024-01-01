from django.shortcuts import render
from django.core import serializers

from timetable.models import Classes,periods
from team.models import Staff
import json 
from django.http import JsonResponse
from active.models import ActiveCourse
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




def index(request):
    test = ActiveCourse.objects.all()

    for active_course_instance in test:
        print(active_course_instance.all_periods_list)

    return render(request, 'timetable/timetable.html',{'test':test})
















def process_schedule(request):

    data = json.loads(request.body)
    teacher_id = data['form']['teacher_id']
    month_id = data['form']['month_id']
    course_id = data['form']['course_id']

    if teacher_id is not None and month_id is None and course_id is None:

        try:
            # Get the Staff object based on the provided teacher_id
            staff = Staff.objects.get(id=teacher_id)

            # Retrieve the periods and courses associated with that teacher
            teacher_periods = staff.periods.all()
            teacher_courses = staff.courses.all()

            # Find all students in other classes who have chosen the same periods and courses
            students_with_shared_periods_courses = Student.objects.filter(
                periods__in=teacher_periods,
                courses__in=teacher_courses
            ).distinct()

            data = serializers.serialize('json', students_with_shared_periods_courses)
            

            return JsonResponse(data, safe=False)
        except Staff.DoesNotExist:
            return JsonResponse({'error': 'Teacher not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid input'}, status=400)









def findTeacher(request):

    data = json.loads(request.body)
    staff_id = data["selectedOption"]

    staff = Staff.objects.get(id=staff_id)

    active_courses = ActiveCourse.objects.filter(teacher=staff)



    free_periods = staff.periods.all()
    active_periods = periods.objects.filter(activecourse__in=active_courses)



    pass 
    # return JsonResponse({"success": True})


