# Generated by Django 4.2.5 on 2023-09-30 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '0006_answerlist_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
