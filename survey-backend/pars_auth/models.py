import random
import string
import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):

    def create(self, **kwargs):
        return self.create_user(**kwargs)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    # name = models.CharField(max_length=40, default=None, null=True)
    # surname = models.CharField(max_length=40, default=None, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    # is_email_confirmation = models.BooleanField(default=False)

    username = models.CharField(max_length=10, default=None, blank=True, null=True, unique=False, primary_key=False)

    email = models.EmailField(verbose_name='email address', max_length=255, primary_key=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    email_confirmation = models.OneToOneField('EmailConfirmation',
                                              on_delete=models.CASCADE,
                                              related_name='user_email_confirmations',
                                              null=True, blank=True, default=None)

    def create_email_confirmation_token(self):
        self.email_confirmation = EmailConfirmation.objects.create(
            user=self
        )
        self.save()

    def __str__(self):
        return self.email


class EmailConfirmation(models.Model):
    user = models.OneToOneField('User',
                                on_delete=models.CASCADE,
                                related_name='email_confirmations',
                                null=True, blank=True, default=None)
    status_choices: list = [
        ('c', 'e-mail confirmed'),
        ('u', 'e-mail un confirmed'),
        ('e', 'e-mail ejected'),
    ]
    status = models.CharField(choices=status_choices, max_length=1, default='u')
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, unique_for_date=True)
    census_token = models.CharField(max_length=145, default=None, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def create_random_census_token(self, row=140):
        characters = string.ascii_letters + string.digits
        token = 'PARS@' + ''.join(random.choice(characters) for _ in range(row))
        self.census_token = token
        self.save()

    def get_status(self):
        status_mapping = dict(self.status_choices)
        return status_mapping.get(self.status, 'Unknown Status')

    def __bool__(self):
        return self.status == 'c'  # confirmed


class BaseToken(models.Model):
    class TokenType:
        login_with_token = 'lwt'
        password_reset_token = 'pwr'

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, unique_for_date=True)
    last_update = models.DateTimeField(auto_now=True)
    token_type_choices = [
        ('pwr', 'Password Reset Token'),
        ('lwt', 'Login With Token'),
    ]
    token_type = models.CharField(choices=token_type_choices, max_length=3)

    @staticmethod
    def create_random_census_token(row=140):
        characters = string.ascii_letters + string.digits
        return 'PARS@' + ''.join(random.choice(characters) for _ in range(row))

    def get_status(self):
        status_mapping = dict(self.token_type_choices)
        return status_mapping.get(self.token_type, 'Unknown Status')

    def __str__(self):
        return f"{self.user.email}# {self.confirmation_token}"

