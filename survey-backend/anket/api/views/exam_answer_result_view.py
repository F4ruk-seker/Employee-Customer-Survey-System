from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from anket.api.serializers import ExamAnswerListSerializers
from anket.models import AnswerList


class ExamAnswerResultView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = AnswerList.objects.all()
    serializer_class = ExamAnswerListSerializers

