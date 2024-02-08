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


from django.http import JsonResponse, HttpResponse

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
    response = HttpResponse()

    print(2323232323)

    data = json.loads(request.body)


    formData_cookie = request.COOKIES.get('formData')

    formData = json.loads(formData_cookie)

    assign_pupl_teacher(data=formData,exam_result=data)


    # # # after submiiting the data delete the cookie in order to resubmit again   
    # response = HttpResponse()
    # expiration_date = datetime(1970, 1, 1)
    # response.set_cookie('formData', value='', expires=expiration_date, httponly=True)

    

    
    return JsonResponse({'message': 'The student is already enrolled'})





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

    # Rest of your code remains the same
    instructor_id_with_less_count = instructor.get_instructor_with_less_count()
    
    activecourse, created_1 = ActiveCourse.objects.get_or_create(
        course=course,
        teacher=instructor_id_with_less_count,
        start_date=start_date,
    )

    activestudent, created_2 = pupl.objects.get_or_create(
        active=activecourse,
        phone=phone,
        name=name,
        email=email,
    )

    if created_2:
        activecourse.enrolled = activecourse.enrolled + 1
        activecourse.save()

    if created_2:

               
        activeexam, created_1 = Exam.objects.get_or_create(
            exam_name=course,
            pupil=activestudent,
            start_date=start_date,
        )



        print(exam_result['form']['answers'])
        answers = exam_result['form']['answers'] #[{'question_id': '3', 'answer_id': '8'}, {'question_id': '2', 'answer_id': '5'}, {'question_id': '5', 'answer_id': '14'}]
        for answer in answers:

            print(666666666666666666666666666666666666666666)

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

        # activeexam, created_1 = ActiveCourse.objects.get_or_create(
        #     exam_name=course,
        #     pupil=activestudent,
        #     start_date=start_date,
        # )


    return 'submitted'