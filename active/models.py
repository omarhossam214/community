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



#
from django.db.models import Count







class instructor(models.Model):
    
    name = models.CharField(max_length=100,unique=True)
    mobile = models.CharField(max_length=100,  blank=True, null=True)
    email = models.CharField(max_length=100,  blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True, null=True)
    periods = models.ManyToManyField(periods, blank=True, null=True)
    count = models.IntegerField(null=True,blank=True,default = 0)

 
    @classmethod
    def get_instructor_with_less_count(cls):
        """
        Get the ID of the instructor with the least count among all assigned instructors.
        """
        instructors_with_counts = cls.objects.exclude(count__isnull=True).order_by('count')

        if instructors_with_counts.exists():
            return instructors_with_counts.first()

        return 'we got nothing to show'
    
    def save(self, *args, **kwargs):

        self.count = ActiveCourse.objects.filter(teacher=self.pk,active=True).count()
        print(232323232)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    





class ActiveCourse(models.Model):

    course_class_id = models.CharField(max_length=100,null=True,blank=True)   
    teacher = models.ForeignKey(instructor, on_delete=models.CASCADE,blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    periods = models.ManyToManyField(periods, blank=True, null=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)


    course_type = [
        ("online", "online"),
        ("On site", "On site"),
        ("On site", "On site"),
    ]


    type = models.CharField(max_length=100,choices=course_type ,default='online',null=True)
    active = models.BooleanField(default=True)
    capacity = models.IntegerField(null=True, default=5)
    enrolled  =  models.IntegerField(null=True,blank=True)
    full =  models.BooleanField(default=False)
    payment = models.ImageField(upload_to='payment_images/', blank=True, null=True)


    def save(self, *args, **kwargs):

        self.enrolled = self.get_pupl_total
        self.course_class_id = f"ENG00{self.pk}"

        if self.capacity >= self.enrolled:
            self.full = True
        else:
            self.full = False

        # teacher_count=ActiveCourse.objects.filter(teacher=self.teacher,active=True).count()
        # self.teacher.count = teacher_count
        # self.teacher.save()
        # Call the save method of the associated instructor instance

        
        super().save(*args, **kwargs)

        if self.teacher:
            self.teacher.save()


    @property
    def get_pupl_total(self):
        try:
            enrolled_count = self.pupl_set.count()
            return enrolled_count
        except:
            return 0
        


    

class pupl(models.Model):

    name = models.CharField(max_length=100,null=True)

    phone = models.CharField(max_length=100,null=True)

    email = models.CharField(max_length=100,null=True)

    active = models.ForeignKey(ActiveCourse, on_delete=models.SET_NULL,null=True)

    payment = models.ImageField(upload_to='payment_images/', blank=True, null=True)


    @job
    def send_email_background(self):
        
        base_directory = settings.BASE_DIR

        template_path = os.path.join(base_directory, 'courses', 'email_template.txt')

        with open(template_path, 'r') as file:
            email_content = file.read()

        email_content = email_content.format(course=self.active.course, name=self.name, date='123')


        send_mail(
            f"Welcome to Community! Your Intro Session is Scheduled for {self.active.course.name}!",
            email_content,
            settings.EMAIL_HOST_USER,
            [f'{self.email}'],
            fail_silently=False,
            html_message=email_content,
        )


    def save(self, *args, **kwargs):

        self.send_email_background()

        super().save(*args, **kwargs)
    
 
