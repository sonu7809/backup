# Generated by Django 4.1.4 on 2022-12-22 06:20

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
                ('stuname', models.CharField(max_length=30)),
                ('stuemail', models.CharField(max_length=30)),
                ('stupass', models.CharField(max_length=30)),
            ],
        ),
    ]