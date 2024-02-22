from django.contrib import admin
from .models import *
# Register your models here.




class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of empty answer forms to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    def answers_list(self, obj):
        # Assuming 'Answer' model has a ForeignKey field named 'question'
        answers = Answer.objects.filter(question=obj)
        return '-- '.join([answer.answer_text for answer in answers])

    list_display = ['id', 'question_text', 'answers_list']




class PupilReactionInline(admin.TabularInline):  # or admin.StackedInline
    model = PupilReaction
    extra = 0  # Number of forms to show for PupilReaction

class ExamAdmin(admin.ModelAdmin):
    inlines = [PupilReactionInline]



admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)

admin.site.register(Exam,ExamAdmin)
admin.site.register(PupilReaction)

