from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

from active.models import pupl

from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io
from django.core.files.base import ContentFile

class Exam(models.Model):

    exam_name = models.CharField(max_length=100,null=True)

    pupil = models.ForeignKey(pupl  , on_delete=models.CASCADE,null=True)

    start_date = models.DateTimeField(null=True)

    end_date = models.DateTimeField(null=True)

    degree = models.IntegerField(null=True,default=0)

    exam_file = models.FileField(null=True,blank=True)


    @property
    def total_degree(self):
        # Calculate the total degree based on correctness of answers
        return PupilReaction.objects.filter(exam=self, selected_answers__is_correct=True).count()
    
        
    @property
    def exam_result(self):
        pupil_reactions = PupilReaction.objects.filter(exam=self)

        result = {'questions': [],
                'correct_answers': [],
                'selected_answers': []}

        for pupil_reaction in pupil_reactions:
            question_data = {
                'question_text': pupil_reaction.question.question_text,
                'answers': [{'text': answer.answer_text, 'correct': answer.is_correct} for answer in Answer.objects.filter(question=pupil_reaction.question)],
                'selected_answer': pupil_reaction.selected_answers.answer_text
            }

            result['questions'].append(question_data)
            # result['correct_answers'].append(pupil_reaction.correct_answer.answer_text)
            # result['selected_answers'].append(pupil_reaction.selected_answers.answer_text)

        return result



    def create_pupil_reaction_pdf(self):
        # Get related PupilReaction for this exam
        exam_result  = self.exam_result

        name = self.exam_name

        print(exam_result)

        # Simple HTML content for testing
        html_content = render_to_string('pdf_template.html', {
            'exam_result': exam_result,
            'name':name
        })

      
        # Convert HTML to PDF
        pdf_content = io.BytesIO()

        pisa.CreatePDF(html_content, dest=pdf_content)

        pdf_content.seek(0)


        return pdf_content.read()        # Get related PupilReaction for this exam

        

    def save(self, *args, **kwargs):
        """
        Override the save method to update the degree.
        """
        self.degree = self.total_degree

        if not self.exam_file:
            # Create PupilReaction PDF and save it as exam_file only if it's not already set
            pdf_content = self.create_pupil_reaction_pdf()
            self.exam_file.save(f"{self.exam_name}_pupil_reaction.pdf", ContentFile(pdf_content), save=True)

        super().save(*args, **kwargs)


        # Update exam_file without triggering the save method





class Question(models.Model):

    question_text = RichTextField(null=True, blank=True)


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

    def __str__(self):
        return self.answer_text
    



class PupilReaction(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=True)

    selected_answers = models.ForeignKey(Answer, on_delete=models.CASCADE,null=True)
    
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,null=True)
