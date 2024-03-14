from django.db import models
from courses.models import Course
from timetable.models import periods

# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

#sending email 
from django.conf import settings
from django.core.mail import send_mail
import os
from django.db import models
from django_rq import job


import datetime


#
from django.db.models import Count

from django_summernote.fields import SummernoteTextField


from django_summernote.widgets import SummernoteWidget

from ckeditor.fields import RichTextField




class instructor(models.Model):
    
    name = models.CharField(max_length=100,unique=True)

    mobile = models.CharField(max_length=100,  blank=True, null=True)

    email = models.CharField(max_length=100,  blank=True, null=True)

    courses = models.ManyToManyField(Course, blank=True, null=True)

    periods = models.ManyToManyField(periods, blank=True, null=True)

    count = models.IntegerField(null=True,blank=True,default = 0)

    shifts =  [
       ("Morning", "Morning"),
        ("Night", "Nght"),
        ('Any','Any')
    ]

    ShiftChoices = models.CharField(max_length=100,choices=shifts ,default='Any',null=True)

 
    @classmethod
    def get_instructor_with_less_count(cls):
        """
        Get the ID of the instructor with the least count among all assigned instructors.

        add the course paramater , and the shift paramater 
        """
        instructors_with_counts = cls.objects.exclude(count__isnull=True).order_by('count', 'id')

        if instructors_with_counts.exists():
            return instructors_with_counts.first()

        return 'No instructor in the database Yet, register instructor in order to assign them'
    

    
    @classmethod
    def get_instructor_with_less_count_match_shifts(cls, shift):
        """
        Get the ID of the instructor with the least count among all assigned instructors.

        add the course paramater , and the shift paramater 
        """
        instructors_with_counts = cls.objects.exclude(count__isnull=True).filter(ShiftChoices=shift).order_by('count', 'id')

        if instructors_with_counts.exists():
            return instructors_with_counts.first()

        return 'No instructor in the database Yet, register instructor in order to assign them'
    
    def save(self, *args, **kwargs):

        self.count = ActiveCourse.objects.filter(teacher=self.pk,active=True).count()

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

        
    @property
    def get_unique_dates(self):
        
        """
        Get unique dates associated with the periods of the instructor.
        """
        unique_dates_set = set()

        uniquePeriod = periods.objects.all()

        unique_dates_list = []
        for period in uniquePeriod:
            if period.start_at not in unique_dates_list:
                unique_dates_list.append(period.start_at)
            else :
                pass


        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        return {
            'unique_dates': unique_dates_list,
            'unique_days': days,
        }
  
    
    @property
    def get_active_course(self):

        activeCourse = ActiveCourse.objects.filter(teacher=self)


        return {
            'activeCourse':activeCourse
        }
    
    @property
    def get_active_course_period(self):
        periods_object = []

        periods_list = periods.objects.all()

        for period in periods_list:
            periods_object.append({
                'day': period.day,
                'start_at': period.start_at,
                'end_at': period.end_at,
                'course_id': None,
                'activeCourseId': None  # Initialize activeCourseId to None

            })

        active_periods_object = []

        activeCourse = ActiveCourse.objects.filter(teacher=self)

        # List to track unique periods while preserving order
        unique_periods_list = []

        for course in activeCourse:
            for activePeriod in course.periods.all():
                current_period = {
                    'day': activePeriod.day,
                    'start_at': activePeriod.start_at,
                    'end_at': activePeriod.end_at,
                    'course_id': course.course_class_id,
                    'activeCourseId':course.pk
                }

                # Check if the period is already in the list (a duplicate)
                if current_period not in unique_periods_list:
                    # Add the current period to the list and active_periods_object
                    unique_periods_list.append(current_period)
                    active_periods_object.append(current_period)

        # Update the course_id in periods_object based on active_periods_object
        for period_info in periods_object:
            for active_period in active_periods_object:
                # Check equality based on relevant fields
                if (
                    period_info['day'] == active_period['day'] and
                    period_info['start_at'] == active_period['start_at'] and
                    period_info['end_at'] == active_period['end_at']
                ):
                    period_info['course_id'] = active_period['course_id']
                    period_info['activeCourseId'] = active_period['activeCourseId']


        return periods_object


    
    

class ActiveCourse(models.Model):

    course_class_id = models.CharField(max_length=100,null=True,blank=True)

    teacher = models.ForeignKey(instructor, on_delete=models.CASCADE,blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    periods = models.ManyToManyField(periods, blank=True, null=True, through='ActiveCoursePeriod')

    start_date = models.DateField(null=True, blank=True)

    end_date = models.DateField(null=True,blank=True)


    course_type = [
        ("online", "online"),
        ("On site", "On site"),
    ]


    type = models.CharField(max_length=100,choices=course_type ,default='online',null=True)

    active = models.BooleanField(default=True)

    capacity = models.IntegerField(null=True,default=5)

    enrolled  =  models.IntegerField(null=True,blank=True)

    payment = models.ImageField(upload_to='payment_images/', blank=True, null=True)


    
    shifts =  [
       ("Morning", "Morning"),
        ("Night", "Nght"),
        ('Any','Any')
    ]

    ShiftChoices = models.CharField(max_length=100,choices=shifts ,default='Any',null=True)

 


    def save(self, *args, **kwargs):
        
        self.enrolled = self.get_pupl_total

        self.course_class_id = f"ENG00{self.pk}"

        super().save(*args, **kwargs)

        if self.teacher:
            self.teacher.save()


    @property
    def all_periods_list(self):
        all_periods = periods.objects.all()
        selected_periods = self.periods.all()

        # Create a list of dictionaries with period information and chosen flag
        all_periods_list = [
            {'period': period, 'chosen': period in selected_periods}
            for period in all_periods
        ]
        return all_periods_list


    @property
    def unique_days_and_start_at(self):

        unique_days = []
        unique_start_at = []

        for period_info in self.all_periods_list:
            period = period_info['period']
            if period.day not in unique_days:
                unique_days.append(period.day)
            if period.start_at not in unique_start_at:
                unique_start_at.append(period.start_at)

        return {
            'unique_days': unique_days,
            'unique_start_at': unique_start_at,
        }
    
    
    @property
    def get_pupl_total(self):
        try:
            enrolled_count = self.pupl_set.count()
            return enrolled_count
        except:
            return 0
        
    
    def __str__(self):
        return f"{self.course_class_id} - {self.course}"
 
        
    

class pupl(models.Model):

    name = models.CharField(max_length=100,null=True)

    phone = models.CharField(max_length=100,null=True)

    email = models.CharField(max_length=100,null=True)

    active = models.ForeignKey(ActiveCourse, on_delete=models.SET_NULL,null=True)

    payment = models.ImageField(upload_to='payment_images/', blank=True, null=True)

    
    shifts =  [
       ("Morning", "Morning"),
        ("Night", "Nght"),
        ('Any','Any')
    ]

    ShiftChoices = models.CharField(max_length=100,choices=shifts ,default='Any',null=True)

 


    def send_email_enrollment(self):
        
        base_directory = settings.BASE_DIR



        template_path = os.path.join(base_directory, 'emails', 'enrollment.txt')

        with open(template_path, 'r') as file:
            email_content = file.read()


        email_content = email_content.format(
            course=self.active.course, name=self.name, date=self.active.start_date,Instructor_Name = self.active.teacher.name
            )


        send_mail(
            f"Welcome to Community! Your Intro Session is Scheduled for {self.active.course.name}!",
            email_content,
            settings.EMAIL_HOST_USER,
            [f'{self.email}'],
            fail_silently=False,
            html_message=email_content,
        )

 

    def save(self, *args, **kwargs):

        self.send_email_enrollment()

        super().save(*args, **kwargs)
    
 






class ActiveCoursePeriod(models.Model):

    active_course = models.ForeignKey(ActiveCourse, on_delete=models.CASCADE)

    period = models.ForeignKey(periods, on_delete=models.CASCADE)

    teacher = models.ForeignKey(instructor, on_delete=models.CASCADE,blank=True, null=True)

    content = RichTextField(null=True, blank=True)

    class Meta:
        unique_together = ('teacher', 'period')



    def save(self, *args, **kwargs):
        if not self.teacher and self.active_course:
            self.teacher = self.active_course.teacher
        super().save(*args, **kwargs)




class Attendance(models.Model):


    student = models.ManyToManyField(pupl, through='AttendanceRecord')

    active_course = models.ForeignKey(ActiveCourse, on_delete=models.CASCADE,null=True)

    date = models.DateField(null=True)

    class_created = models.BooleanField(null=True,default=False)

    def __str__(self):
        return f"attendance of {self.active_course.course} - {self.date} ---  ID : {self.pk}"
 
    @property
    def assign_course_classes_count(self):

        if self.class_created == False:
            count = self.active_course.course.coursedetails.chapter_count()

            students = pupl.objects.filter(active=self.active_course)

            # Create instances based on the count
            for student in students:
                for _ in range(count):
                    # You may customize the creation logic based on your requirements
                    AttendanceRecord.objects.create(attendance=self, student=student)  # Add appropriate values for the fields

    @property
    def get_course_classes_count(self):

        count = self.active_course.course.coursedetails.chapter_count()

        return count

   

    def save(self, *args, **kwargs):

        if self.class_created == False:
            super().save(*args, **kwargs)
            self.assign_course_classes_count
            self.class_created = True

        super().save(*args, **kwargs)



    #create a method that return AttendanceRecord that related to the same active course @property
        #### to-do update the Date to the Dict data that being send  ##### 
    @property
    def get_AttendanceRecord(self):
         
        attendance_records = AttendanceRecord.objects.filter(attendance=self)

        student_attendance = []

        for record in attendance_records:
            student_id = record.student.id  # Assuming 'id' is the field for student ID

            # Check if the student is already in the list
            existing_student = next((student for student in student_attendance if student['student_id'] == student_id), None)

            if existing_student:
                # Student is already in the list, append class information
                existing_student['class'].append({
                    'class_status': record.attended,
                    'class_id': record.id  
                })
            else:
                # Student is not in the list, add a new entry
                student_attendance.append({
                    'student_name': record.student.name,  
                    'student_id': student_id,
                    'class': [{
                        'class_status': record.attended,
                        'class_id': record.id  
                    }]
                })

        return student_attendance

        
    
class AttendanceRecord(models.Model):

    student = models.ForeignKey(pupl, on_delete=models.CASCADE,null=True)

    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE,null=True)
    
    ATTENDANCE_CHOICES = [
        ('not chosen','Not chosen'),
        ('attended', 'Attended'),
        ('cancelled_teacher', 'Cancelled by Teacher'),
        ('cancelled_student', 'Cancelled by Student'),
    ]

    attended = models.CharField(max_length=20, choices=ATTENDANCE_CHOICES, default='not chosen',null=True)

    date = models.DateField(null=True)


    content = RichTextField(null=True, blank=True)



    def __str__(self):
        return f"attendance of {self.student} - {self.attended} ---  ID : {self.attendance.active_course}"
 