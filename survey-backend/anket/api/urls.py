from django.urls import path, include
from anket.api.views import ExamView, ExamsListView, ExamAnswerView, ExamAnswerResultView


app_name = "exam_api"


urlpatterns = [
    path('', ExamsListView.as_view()),
    path('answers/', ExamAnswerResultView.as_view()),
    path('<slug>/', ExamView.as_view()),
    path('<slug>/answer/', ExamAnswerView.as_view()),

]

