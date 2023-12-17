from django.contrib import admin
from .models import *
# Register your models here.
from django import forms
from django.db import models
from django.forms.widgets import Textarea





admin.site.register(Curriculum)
admin.site.register(Module)
admin.site.register(Chapter)
admin.site.register(CourseDetails)
admin.site.register(Audience)
admin.site.register(Requirement)



