# Generated by Django 3.1.3 on 2020-12-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20201206_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_instructions',
        ),
        migrations.AddField(
            model_name='question',
            name='question_description',
            field=models.TextField(default=''),
        ),
    ]
