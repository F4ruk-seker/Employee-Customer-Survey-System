# Generated by Django 4.2.5 on 2023-11-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pars_auth', '0004_basetoken_delete_logintoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetoken',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
