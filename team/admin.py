from django.contrib import admin, messages
from .models import *

from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta



from django.contrib import admin
from django.utils import timezone
from datetime import datetime, timedelta
from timetable.models import periods 
from.models import *




class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'index_link')



admin.site.register(Student)
admin.site.register(Staff,StaffAdmin)