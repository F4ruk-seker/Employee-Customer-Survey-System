from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
import os


def turkish_charset_convert(text_or_instance):
    if isinstance(text_or_instance, str):
        text = text_or_instance
    elif isinstance(text_or_instance, Exam):
        text = text_or_instance.title
    else:
        return text_or_instance  # Return unchanged if not a string or Exam instance

    text = text.replace('ı', 'i')
    text = text.replace('ş', 's')
    text = text.replace('ğ', 'g')
    text = text.replace('ü', 'u')
    text = text.replace('ö', 'o')
    text = text.replace('ç', 'c')

    return text


class Exam(models.Model):
    title = models.TextField()
    slug = AutoSlugField(populate_from=turkish_charset_convert, editable=True, always_update=True)
    questions = models.ManyToManyField('anket.Question')

    def get_questions(self):
        return self.questions.all()

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    answers = models.ManyToManyField('anket.Answer', blank=True)

    def __str__(self):
        return self.text[:30] + '...' if len(self.text) > 30 else self.text

    @classmethod
    def load_defaults(cls):
        if os.path.isfile('questions.txt'):
            questions_file = open("questions.txt", "r", encoding='utf-8')
            questions = questions_file.read().split('\n')
            questions_file.close()
            for question in questions:
                cls.objects.create(
                    text=question.strip()
                )
        else:
            raise 'questions.txt file not found'


class Answer(models.Model):
    value = models.PositiveIntegerField()


class AnswerList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # email = models.EmailField(default=None, null=True)
    exam = models.ForeignKey('anket.Exam', on_delete=models.CASCADE)
    answer_question_list = models.ManyToManyField('anket.AnswerQuestionHandle')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'@({self.id}) => {"NaN"} | {self.exam}'


class AnswerQuestionHandle(models.Model):
    question = models.ForeignKey('anket.Question', on_delete=models.CASCADE, null=True, default=None)
    answer = models.ForeignKey('anket.Answer', on_delete=models.CASCADE, null=True, default=None)

