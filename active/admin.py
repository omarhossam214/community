from django.contrib import admin
from .models import *

# Register your models here.
from django.contrib import admin
from .models import ActiveCourse,instructor
from django.utils.html import format_html



class PuplInline(admin.StackedInline):
    model = pupl
    extra = 0





class PuplAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','payment')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('active',)








class ActiveCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'course', 'get_future_date','GetPeriods',"capcity")
    inlines = [PuplInline]


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


#kkkkkk
