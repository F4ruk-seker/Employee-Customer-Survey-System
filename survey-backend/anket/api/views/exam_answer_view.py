from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from anket.api.serializers import AnswerListSerializer
from anket.models import Exam, Answer, AnswerList, AnswerQuestionHandle
import re


class ExamAnswerView(CreateAPIView):
    serializer_class = AnswerListSerializer
    lookup_field = 'slug'

    @staticmethod
    def get_exam_from_slug(slug: str):
        return get_object_or_404(Exam, slug=slug)

    @staticmethod
    def validate_email_address(email_address):
        try:
            return re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email_address)
        except:
            pass

    def post(self, request, *args, **kwargs):
        # email = request.data.get('email')
        # email_is_valid = self.validate_email_address(email)
        exam_slug = kwargs.get('slug')
        if exam_slug:
            exam = self.get_exam_from_slug(exam_slug)
            answer_list = AnswerList()
            answer_list.user = request.user
            answer_list.exam = exam
            # answer_list.email = self.request.user.email
            answer_list.save()
            for base_question in exam.get_questions():
                for client_question in request.data.get('exam').get('questions'):
                    if base_question.id == client_question.get('id'):
                        answer_question_handle = AnswerQuestionHandle.objects.create(
                            answer=Answer.objects.create(value=client_question.get("answer")),
                            question=base_question
                        )
                        answer_list.answer_question_list.add(answer_question_handle)
            answer_list.save()
            return Response({}, 201)
        else:
            return Response({"message": "Unknow fields"}, 406)

