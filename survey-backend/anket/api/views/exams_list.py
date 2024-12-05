from rest_framework.generics import ListAPIView
from anket.models import Exam
from anket.api.serializers import ExamListSerializer
from rest_framework.permissions import IsAuthenticated


class ExamsListView(ListAPIView):
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = ExamListSerializer
    queryset = Exam.objects.all()

