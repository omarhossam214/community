from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

from active.models import pupl




class Exam(models.Model):
    exam_name = models.CharField(max_length=100,null=True)
    pupil = models.ForeignKey(pupl  , on_delete=models.CASCADE,null=True)
    start_date = models.DateTimeField(null=True)
    end_data = models.DateTimeField(null=True)




class Question(models.Model):

    question_text = RichTextField(null=True, blank=True)

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)

    LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2')
    ]

    level = models.CharField(max_length=20,null=True,choices = LEVEL_CHOICES)

    def __str__(self):
        return self.question_text
    
    @property
    def fetch_related_answers(self):
        
        answers = Answer.objects.filter(question=self)

        return answers

class Answer(models.Model):

    answer_text = models.CharField(max_length=200,null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    is_correct = models.BooleanField(default=False)




class PupilReaction(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)
    selected_answers = models.ForeignKey(Answer, on_delete=models.CASCADE,null=True)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True)
