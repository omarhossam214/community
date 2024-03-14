from django.shortcuts import render,get_object_or_404

import json 
from active.models import ActiveCourse,instructor,Attendance,AttendanceRecord
# Create your views here.


from django.forms.models import model_to_dict
import json
from active.models import ActiveCourse

from django.http import HttpResponse

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


        print(attendance_records)


        return render(request, 'attendace/attendace.html',{'attendance_records':attendance_records,'classes':classes})
    

#### waiting to update the method in the AttendanceRecord Class "get_AttendanceRecord" method ##### 
def update_attendance(request):

    data = json.loads(request.body)


    print(data['form']['Class_id'])

    attendance_id = data['form']['Class_id']
    attendance_status = data['form']['Selected_attendance']
    attendance_date = data['form']['Selected_date']


    print(attendance_date) #2024-03-20
    print(type(attendance_date)) # <class 'str'>

    attendance_record = AttendanceRecord.objects.filter(id=attendance_id).first()

    attendance_record.attended = attendance_status

    attendance_record.date = attendance_date

    attendance_record.save()



    print("Updated attendance record with ID:", attendance_id)

    
    return HttpResponse('Done')
