from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from anket.models import Exam


class ExamList(ListView):
    queryset = Exam.objects.all()
    model = Exam
    context_object_name = 'exams'
    template_name = 'exam_list.html'


class ExamView(DetailView):
    model = Exam
    queryset = Exam.objects.all()
    template_name = 'exam.html'
    context_object_name = 'exam'

    # pk_url_kwarg = 'slug'
    # template_name =

    # def get_queryset(self):
    #     if slug := self.kwargs.get('slug'):
    #         return get_object_or_404(Exam, slug=slug)
    #     return {}