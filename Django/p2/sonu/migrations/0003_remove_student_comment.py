# Generated by Django 4.1.4 on 2022-12-21 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sonu', '0002_student_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
    ]
