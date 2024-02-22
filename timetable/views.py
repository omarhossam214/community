from django.shortcuts import render
from django.core import serializers

from timetable.models import Classes,periods
from team.models import Staff
import json 
from django.http import JsonResponse
from active.models import ActiveCourse,instructor
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


# def index(request):
#     # Retrieve all instances of the instructor model
#     instructors = instructor.objects.all()
#     all_periods = periods.objects.all()

#     # Create a list to store teacher information and associated active periods
#     teacher_info_with_periods = []

#     # Create lists to store unique days and unique times
#     unique_days = []
#     unique_times = []

#     # Create OrderedDicts to check for uniqueness and preserve order
#     unique_days_set = OrderedDict()
#     unique_times_set = OrderedDict()

#     # Iterate over all periods to collect unique combinations
#     for period in all_periods:
#         # Check for uniqueness before appending to the list
#         if period.day not in unique_days_set:
#             unique_days_set[period.day] = None
#             unique_days.append({
#                 'unique days': period.day
#             })

#         if period.start_at not in unique_times_set:
#             unique_times_set[period.start_at] = None
#             unique_times.append({
#                 'unique_times': period.start_at
#             })

#     # Iterate over the instructors
#     for teacher_instance in instructors:
#         # Access the related ActiveCourse instances
#         active_courses = ActiveCourse.objects.filter(teacher=teacher_instance)

#         # Create lists to store active periods for the current teacher
#         active_days = []
#         active_times = []

#         # Iterate over unique days
#         for unique_day_data in unique_days:
#             day = unique_day_data['unique days']

#             # Check if the period is in any of the teacher's active courses
#             is_chosen_day = any(
#                 active_course.periods.filter(day=day).exists()
#                 for active_course in active_courses
#             )

#             active_days.append({
#                 'day': day,
#                 'choosen': is_chosen_day,
#                 # Add more fields as needed
#             })

#         # Iterate over unique times
#         for unique_time_data in unique_times:
#             start_at = unique_time_data['unique_times']

#             # Check if the period is in any of the teacher's active courses
#             is_chosen_time = any(
#                 active_course.periods.filter(start_at=start_at).exists()
#                 for active_course in active_courses
#             )

#             active_times.append({
#                 'start_at': start_at,
#                 'choosen': is_chosen_time,
#                 # Add more fields as needed
#             })

#         # Add teacher information and associated active periods to the list
#         teacher_info_with_periods.append({
#             'teacher': teacher_instance,
#             'active_days': active_days,
#             'active_times': active_times,
#         })

#     # Pass the data to the template
        
#         print(teacher_info_with_periods)

#     return render(request, 'timetable/timetable.html', {'teacher_info_with_periods': teacher_info_with_periods,'active_days':active_days,'active_times':active_times})






#unique_dates
#get_unique_dates


def index(request):

    # Retrieve all instances of the instructor model
    instructors = instructor.objects.all()

    print(instructor)


    return render(request, 'timetable/timetable.html', {'instructors': instructors})








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


