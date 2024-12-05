from django.db.models.signals import post_save
from django.dispatch import receiver
from pars_auth.models import User, EmailConfirmation, BaseToken
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from config.settings.settings_base import PRODUCT_HOST_URL


@receiver(post_save, sender=User)
def send_email_confirmation_mail(sender, created, instance, *args, **kwargs):
    if created:
        instance.create_email_confirmation_token()

        html_content = render_to_string('email_confirmation.html', {
            'confirm_url': f'{PRODUCT_HOST_URL}auth/email/confirmation/{instance.email_confirmation.confirmation_token}/?census_token={instance.email_confirmation.census_token}',
            'email_confirmation_token': instance.email_confirmation.confirmation_token,
            'census_token': instance.email_confirmation.census_token,
            'user': instance
        })
        html_text = strip_tags(html_content)
        msg = EmailMultiAlternatives('Eirişim için e-mailinizi onaylayın ', html_text,
                                     'settings.EMAIL_HOST_USER', (instance.email,))
        # msg.attach(image)

        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=EmailConfirmation)
def create_random_census_token(sender, created, instance, *args, **kwargs):
    if created:
        instance.create_random_census_token()


@receiver(post_save, sender=BaseToken)
def send_token_mail(sender, created, instance, *args, **kwargs):
    if created:
        if instance.token_type == instance.TokenType.login_with_token:
            html_content = render_to_string('login_with_token_mail.html', {
                'confirm_url': f'{PRODUCT_HOST_URL}auth/login/'
                               f'?login_token={instance.confirmation_token}'
                               f'&census_token={instance.create_random_census_token()}',
                'user': instance.user,
                'mail_created_date': instance.last_update
            })
            message = 'E-posta ile Şifresiz Giriş 🔑🔒'
        elif instance.token_type == instance.TokenType.password_reset_token:
            html_content = render_to_string('password_reset_mail.html', {
                'confirm_url': f'{PRODUCT_HOST_URL}auth/reset_password/'
                               f'?reset_token={instance.confirmation_token}'
                               f'&census_token={instance.create_random_census_token()}',
                'user': instance.user,
                'mail_created_date': instance.last_update
            })
            message = 'Şifre Sıfırlama isteği 🔑🔒'
        else:
            return

        html_text = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            message,
            html_text,
            'settings.EMAIL_HOST_USER',
            (instance.user.email,)
        )

        # msg.attach(image)

        msg.attach_alternative(html_content, "text/html")
        msg.send()

