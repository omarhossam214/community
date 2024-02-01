from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
# Create your models here.


from datetime import datetime, timedelta


from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver






class Classes(models.Model):

    name = models.CharField(max_length=100)
    numberOfPeriods = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(16)],default=5)
    numOfweek = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(52)],default=7)

    def __str__(self):
        de = str(self.numOfweek)
        return de

    def save(self, *args, **kwargs):

        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        is_new = not self.pk

        super().save(*args, **kwargs)

        if is_new:
            start_time = datetime(
                year=datetime.today().year,
                month=datetime.today().month,
                day=datetime.today().day,
                hour=9,
            )

            for a in days_of_week:

                for i in range(self.numberOfPeriods):
                        
                        period_name = f"period{i+1}"

                        period_start_time = start_time + timedelta(hours=i)

                        period_end_time = start_time + timedelta(hours=i + 1)

                        is_night_shift = period_start_time.hour >= 18






                        period_week_number = period_start_time.isocalendar()[1]

                        day_name = a 
                        
                        period = periods(

                            Classes=self,
                            name=period_name,
                            start_at=period_start_time,
                            end_at=period_end_time,
                            day = day_name, 

                        )

                        period.ShiftChoices = 'Night' if is_night_shift else 'Morning'
 
                        period.save()
                        
            self.numOfweek = period_week_number
            self.save()




     

class periods(models.Model):

    Classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='Classes',null=True)
    
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES,null=True)

    name = models.CharField(max_length=100,null=True)

    start_at = models.TimeField(null=True)

    end_at = models.TimeField(null=True, blank=True)

    
    
    shifts =  [
       ("Morning", "Morning"),
        ("Night", "Nght"),
        ('Any','Any')
    ]

    ShiftChoices = models.CharField(max_length=100,choices=shifts ,default='Any',null=True)




    def __str__(self):
        return f"{self.day} {self.start_at}"
    
    def get_future_date(self):

        today = datetime.date.today()
        our_day = self.day

        day = today.strftime("%A")

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        if days.index(our_day) < days.index(day):
            diff = 7 - days.index(day) + days.index(our_day)
        else:
            diff = days.index(our_day) - days.index(day)

        future_date = today + datetime.timedelta(days=diff)
        formatted_date = future_date.strftime("%d %B")

        return formatted_date
    
    def class_time(self):
        return f'{self.start_at} - {self.end_at}'
    
 
    