from django.urls import path, include
from anket.views import ExamList, ExamView


app_name = "exam"


urlpatterns = [
    path('', ExamList.as_view()),
    path('<slug>/', ExamView.as_view()),
]

