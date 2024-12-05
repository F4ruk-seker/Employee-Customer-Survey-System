from rest_framework import serializers
from anket.models import Exam, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = '__all__'
        fields = 'id', 'text'


class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'


class ExamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ('id', 'title', 'slug')
