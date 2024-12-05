from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from anket.api.serializers import ExamSerializer
from anket.models import Exam


class ExamView(RetrieveAPIView):
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = 'slug'

