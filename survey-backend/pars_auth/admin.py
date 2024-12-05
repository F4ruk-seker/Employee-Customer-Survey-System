"""
coder : f4
inspiration:
https://github.com/jmfederico/django-use-email-as-username/tree/main
"""


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, EmailConfirmation, BaseToken
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_superuser")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("is_superuser", "email")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
            ('Email Confirmation Fields', {
                 'fields': (
                     'email_confirmation',
                     'display_email_confirmation_confirm',
                     'display_email_confirmation_token',
                     'display_email_confirmation_census_token',
                     'display_email_confirmation_last_update',
                 )
              }),

    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "first_name", "password1", "password2")}),
    )

    readonly_fields = (
        'display_email_confirmation_confirm',
        'display_email_confirmation_token',
        'display_email_confirmation_census_token',
        'display_email_confirmation_last_update',
    )

    def display_email_confirmation_confirm(self, obj):
        return obj.email_confirmation.get_status()

    def display_email_confirmation_token(self, obj):
        return obj.email_confirmation.confirmation_token

    def display_email_confirmation_last_update(self, obj):
        return obj.email_confirmation.last_update

    def display_email_confirmation_census_token(self, obj):
        return obj.email_confirmation.census_token

    display_email_confirmation_confirm.short_description = 'Email Confirmation Status'
    display_email_confirmation_token.short_description = 'Email Confirmation Token'
    display_email_confirmation_census_token.short_description = 'Email Confirmation Census Token'
    display_email_confirmation_last_update.short_description = 'Email Confirmation Last Update'


admin.site.register(User, CustomUserAdmin)

admin.site.register(BaseToken)
admin.site.register(EmailConfirmation)

