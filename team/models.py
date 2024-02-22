from django.db import models
from courses.models import Course
from timetable.models import periods



from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse
from django.utils.html import format_html

from active.models import instructor


class Staff(models.Model):

    name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='staff_images/', blank=True, null=True)
    
    title_type = [('instructor','instructor'),
                  ('Not intstuctor','Not intstuctor')]
    
    title = models.CharField(max_length=100,choices = title_type , null = True)
    overview = models.TextField(null=True,blank=True)
    # certifcation = models.ImageField(upload_to='staff_images/', blank=True, null=True)

    facebook = models.CharField(max_length=100,  blank=True, null=True)
    twitter = models.CharField(max_length=100,  blank=True, null=True)
    email = models.CharField(max_length=100,  blank=True, null=True)
    mobile = models.CharField(max_length=100,  blank=True, null=True)

    courses = models.ManyToManyField(Course, blank=True, null=True)
    periods = models.ManyToManyField(periods, blank=True, null=True)




    def save(self, *args, **kwargs):

        if self.title == 'instructor':

                instructor_instance,  created_2 = instructor.objects.get_or_create(name = self.name,
                                                               email = self.email,
                                                               mobile = self.mobile,
                                                               )
                
            
                instructor_instance.courses.set(self.courses.all())


        super().save(*args, **kwargs)





    def __str__(self):
        return self.name
    
    def index_link(self):
        return format_html('<a href="{}">Timetable</a>', '/timetable')

    index_link.short_description = 'time table'

    
   



class Certifcation(models.Model):

    award = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='award')
    photo = models.ImageField(upload_to='images',null=True)



class Student(models.Model):

    

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    #periods = models.ManyToManyField(periods, null=True)

    

    def __str__(self):
        return self.name
    
    # def assign_staff(self):
    #     # Get the periods and course selected by the student
    #     periods = self.periods.all()
    #     course = self.courses

    #     # Get the staff that have selected the same periods and course
    #     staff = Staff.objects.filter(periods__in=periods, courses=course)

    #     # Assign the staff to the student if available
    #     for s in staff:
    #         if s.availability:
    #             self.staff.add(s)
    #             s.availability = False
    #             s.save()
    #             break
