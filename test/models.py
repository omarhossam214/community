from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    # Add other fields as needed

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    # Add other fields as needed

    