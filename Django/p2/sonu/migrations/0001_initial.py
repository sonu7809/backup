0
# Generated by Django 4.1.4 on 2022-12-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.CharField(max_length=70)),
                ('stupass', models.CharField(max_length=70)),
            ],
        ),
    ]
