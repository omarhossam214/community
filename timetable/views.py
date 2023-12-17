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

import json





# def index(request):
# #     data = []
# #     json_data = []

# #     df = pd.DataFrame(columns=['Future Date', 'Course', 'Students', 'Teacher'])

# #     today = datetime.date.today()


# #     active_courses = ActiveCourse.objects.all()  # Sort by periods' start_at field
# #     teacher = Staff.objects.all()
# #     courses = Course.objects.all()

# #     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# #     months = [
# #     "January", "February", "March", "April", "May", "June",
# #     "July", "August", "September", "October", "November", "December"
# # ]
# #     period = periods.objects.all()
# #     staff  = Staff.objects.all()


# #     for i in active_courses:
    
# #         students = i.student.all()
# #         stud = []
# #         for student in students:
# #             stud.append(student.name)

# #         pers = i.periods.all()
# #         for a in pers: 
# #             future_date = parser.parse(a.get_future_date())  
# #             start_time = a.start_at  

# #             hour = start_time.hour
# #             minute = start_time.minute

# #             future_date = future_date.replace(hour=hour, minute=minute)

         

# #             data.append({
# #                             'Future Date': future_date.strftime("%A, %d %B %Y %H:%M"),
# #                             'Course': i.course.name,
# #                             'Students': stud,
# #                             'Teacher': i.teacher.name
# #                         })
            
# #         sorted_data = sorted(data, key=lambda x: x['Future Date'])


# #     json_data = json.dumps(sorted_data)
# #     print(type(json_data))

#     return render(request, 'timetable/timetable.html')






def index(request):

    return render(request, 'timetable/timetable.html')




















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


