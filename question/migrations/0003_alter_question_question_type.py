# Generated by Django 5.1 on 2024-08-15 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_question_options_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_type', to='question.questiontype'),
        ),
    ]
