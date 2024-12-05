from rest_framework import serializers
from anket.models import AnswerList
from .exam_serializer import ExamSerializer
from .exam_answer_serializer import AnswerListSerializer, QuestionLink, AnswerQuestionHandleSerializer


class ExamAnswerListSerializers(serializers.ModelSerializer):
    exam = ExamSerializer()
    answer_question_list = AnswerQuestionHandleSerializer(many=True)
    # answer_question_list =

    # def get_answer_question_list(self, obj):
    #     print()
    #     return AnswerListSerializer(obj.answer_question_list.all(), many=True).data

    class Meta:
        model = AnswerList
        fields = '__all__'

