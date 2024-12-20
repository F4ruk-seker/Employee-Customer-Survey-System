# Generated by Django 4.2.5 on 2023-09-29 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '0003_remove_answerlist_user_answerlist_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerlist',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='answerlist',
            name='questions',
        ),
        migrations.CreateModel(
            name='AnswerQuestionHandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.ManyToManyField(to='anket.answer')),
                ('questions', models.ManyToManyField(to='anket.question')),
            ],
        ),
        migrations.AddField(
            model_name='answerlist',
            name='answer_question_list',
            field=models.ManyToManyField(to='anket.answerquestionhandle'),
        ),
    ]
