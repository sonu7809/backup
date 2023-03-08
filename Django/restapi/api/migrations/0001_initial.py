# Generated by Django 4.1.4 on 2022-12-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('nonit', 'nonit'), ('mobile', 'mobile')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
