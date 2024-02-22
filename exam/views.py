from django.shortcuts import render
from .models import Question
from random import sample
import json
from datetime import datetime, timedelta
from django.http import HttpResponse
from team.models import instructor
from active.models import pupl
from active.models import ActiveCourse
from django.shortcuts import get_object_or_404

from courses.models import Course 
from.models import Exam,PupilReaction,Answer
# Create your views here.
from django.core.files.base import ContentFile


from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import os


def index(request):
    # Fetch three questions randomly

    try:

        formData_cookie = request.COOKIES.get('formData')

        formData = json.loads(formData_cookie)

        name = formData['form']['Name']

        email = formData['form']['Email']


        questions = sample(list(Question.objects.all()), 3)

        return render(request, 'exam/exam.html', {'questions': questions,'name':name,'email':email})
    
    except:
        return render(request, 'index/index.html')



def get_student_answers(request):


    data = json.loads(request.body)


    formData_cookie = request.COOKIES.get('formData')
    formData = json.loads(formData_cookie)

    assign_pupl_teacher(data=formData,exam_result=data)

   # Clear the formData cookie
    response = HttpResponse()
    expiration_date = datetime(1970, 1, 1)
    response.set_cookie('formData', value='', expires=expiration_date, httponly=True)

    print('DONE')

    
    return response





def assign_pupl_teacher(data,exam_result):

    # Extract data from the JSON payload
    name = data['form']['Name']
    phone = data['form']['Phone']
    email = data['form']['Email']
    start_date = data['form']['startDate']
    shift = data['form']['shift']
    course = data['form']['course_id'] #return course ID 

    course = get_object_or_404(Course, pk=course)
    # Convert the course dictionary back to a Course object

    print(shift)

    # Get_instructor_with_less_count_match_shifts
    instructor_id_with_less_count = instructor.get_instructor_with_less_count_match_shifts(shift = shift)
    
    activecourse, created_1 = ActiveCourse.objects.get_or_create(
        course=course,
        teacher=instructor_id_with_less_count,
        start_date=start_date,
        ShiftChoices=shift
    )

    activestudent, created_2 = pupl.objects.get_or_create(
        active=activecourse,
        phone=phone,
        name=name,
        email=email,
        ShiftChoices=shift
    )

    if created_2:
        activecourse.enrolled = activecourse.enrolled + 1
        activecourse.save()

    if created_2:

               
        activeexam, created_1 = Exam.objects.get_or_create(
            exam_name=course.name, # Use the name attribute of the Course
            pupil=activestudent,
            start_date=start_date,
        )



        answers = exam_result['form']['answers'] 
        for answer in answers:


            question_id = answer['question_id']
            answer_id = answer['answer_id']

            # Fetch the Question and Answer instances based on the provided IDs
            question = get_object_or_404(Question, pk=question_id)
            selected_answer = get_object_or_404(Answer, pk=answer_id)

            # Create a PupilReaction instance and associate it with the ActiveExam, Question, and Answer
            pupil_reaction, created_2 = PupilReaction.objects.get_or_create(
                question=question,
                selected_answers=selected_answer,
                exam=activeexam,
            )

    if created_1:
            # Create PupilReaction PDF and save it as exam_file only if it's not already set
            pdf_content = activeexam.create_pupil_reaction_pdf()
            activeexam.exam_file.save("pupil_reaction.pdf", ContentFile(pdf_content), save=True)

            activeexam.save()

            activeexam.send_exam_result_email()


    #activestudent


    return JsonResponse({'data': {'message': 'Done'}})



