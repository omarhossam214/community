from django.contrib import admin
from .models import *

# Register your models here.
from django.contrib import admin
from .models import ActiveCourse,instructor,ActiveCoursePeriod
from django.utils.html import format_html
from django.urls import reverse
from django.utils.html import format_html



class PuplInline(admin.StackedInline):
    model = pupl
    extra = 0





class PuplAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','payment')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('active',)








class ActiveCoursePeriodInline(admin.TabularInline):  # or admin.StackedInline
    model = ActiveCoursePeriod
    exclude = ['content']
    extra = 1  # Set the number of inline forms to display










class ActiveCourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'teacher', 'course', 'get_future_date','GetPeriods',"capcity")
    inlines = [PuplInline,ActiveCoursePeriodInline]
    list_display = ['course_class_id', 'teacher_name', 'view_active_course_periods']

    
    def teacher_name(self, obj):
        return obj.teacher.name if obj.teacher else None
    
    def view_active_course_periods(self, obj):
        url = reverse('admin:active_activecourseperiod_changelist')
        return format_html('<a href="{}?active_course__id={}">View ActiveCoursePeriods</a>', url, obj.id)

    def capcity(self, obj):
        show = str(obj.get_pupl_total) + '/' + str (obj.capacity)
        return show

    
    def get_future_date(self, obj):
        periods = obj.periods.all()
        future_dates = []
        for period in periods:
            future_dates.append(period.get_future_date())  
            
        return ', '.join(future_dates)  

    get_future_date.short_description = 'Future Dates'  


    def GetPeriods(self,obj):

        periods = obj.periods.all()
        dates = []

        for period in periods:
            dates.append(str(period))
            
        return ', '.join(dates)
            
    GetPeriods.short_description = 'Dates'


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'count')
    list_filter = ('courses', 'periods')













admin.site.register(ActiveCourse, ActiveCourseAdmin)
admin.site.register(pupl,PuplAdmin)
admin.site.register(instructor,InstructorAdmin)
admin.site.register(ActiveCoursePeriod)


#kkkkkk
