from django.db import models
from courses.models import *
# Create your models here.



# class Audience(models.Model):
#     name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.name
    

    
# class Requirement(models.Model):
#     name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.name
    





# class Curriculum(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     def __str__(self):
#         return self.name

# class Module(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     curriculum = models.ForeignKey(Curriculum, related_name='modules', on_delete=models.CASCADE, null=True)
    
#     def __str__(self):
#         return self.name

# class Chapter(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     module = models.ForeignKey(Module, related_name='chapters', on_delete=models.CASCADE, null=True)
    
#     def __str__(self):
#         return self.name

# class Requirement(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     def __str__(self):
#         return self.name

# class Audience(models.Model):
#     name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name

# class CourseDetails(models.Model):
#     course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True)
#     overview = models.TextField(null=True)
#     requirements = models.ManyToManyField(Requirement)
#     audience = models.ManyToManyField(Audience)
#     curriculum = models.OneToOneField(Curriculum, on_delete=models.CASCADE, null=True)
#     duration = models.CharField(max_length=50, null=True)







class Audience(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Requirement(models.Model):

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name



class Chapter(models.Model):
    
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name



class Module(models.Model):

    name = models.CharField(max_length=255, null=True)
    Chapter = models.ManyToManyField(Chapter, related_name='chapter')

    def __str__(self):
        return self.name

class Curriculum(models.Model):

    name = models.CharField(max_length=255, null=True)
    module = models.ManyToManyField(Module, related_name='module')
    
    def __str__(self):
        return self.name
    

class CourseDetails(models.Model):

    price = models.IntegerField(null=True)
    overview = models.TextField(null=True)
    requirements = models.ManyToManyField(Requirement)
    audience = models.ManyToManyField(Audience)
    curriculum = models.OneToOneField(Curriculum, on_delete=models.CASCADE, null=True)
    duration = models.CharField(max_length=50, null=True)


    def old_price(self):
        old_price = self.price - 100
        return old_price


    def module_count(self):
        return self.curriculum.module.count()
    
    
    def chapter_count(self):
        total_chapters = 0
        for module in self.curriculum.module.all():
            total_chapters += module.Chapter.count()
        return total_chapters