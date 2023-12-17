from django.db import models
from courseDetail.models import CourseDetails
# Create your models here.



class Course(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images',null=True)
    coursedetails = models.OneToOneField(CourseDetails, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    
