# Generated by Django 2.2.1 on 2019-06-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
    ]
