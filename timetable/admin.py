from django.contrib import admin
from.models import *
# Register your models here.



class PeriodsInline(admin.TabularInline):
    model = periods
    extra = 0
    can_delete = True

class ClassesAdmin(admin.ModelAdmin):
    inlines = [PeriodsInline]





admin.site.register(Classes, ClassesAdmin)
admin.site.register(periods)

