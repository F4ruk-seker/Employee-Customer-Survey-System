from rest_framework import serializers
from anket.models import AnswerList, AnswerQuestionHandle


class QuestionLink(serializers.Serializer):
    question = serializers.IntegerField()  # id
    answer = serializers.IntegerField()  # value


class AnswerListSerializer(serializers.ModelSerializer):
    question_link = QuestionLink(many=True)

    class Meta:
        model = AnswerList
        fields = ('user', 'exam', 'question_link')


class AnswerQuestionHandleSerializer(serializers.ModelSerializer):

    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    def get_question(self, obj):
        return obj.question.text

    def get_answer(self, obj):
        return obj.answer.value

    class Meta:
        model = AnswerQuestionHandle
        fields = '__all__'

