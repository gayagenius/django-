# Generated by Django 2.2.1 on 2019-06-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_remove_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]