from django.db.models.signals import post_save
from django.dispatch import receiver
from anket.models import AnswerList
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save, sender=AnswerList)
def send_exam_results_to_user(sender, created, instance, *args, **kwargs):
    if not created:

        html_content = render_to_string('survey_result.html', {
            'answer_question_list': instance.answer_question_list.all(),
            'exam': instance.exam,
            'created': instance.created
        })

        html_text = strip_tags(html_content)
        msg = EmailMultiAlternatives('Anket Sonuç', html_text,
                                     'settings.EMAIL_HOST_USER', (instance.user.email,))
        # msg.attach(image)

        msg.attach_alternative(html_content, "text/html")
        msg.send()

