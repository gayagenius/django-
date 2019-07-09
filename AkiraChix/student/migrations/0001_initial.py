# Generated by Django 2.2.1 on 2019-05-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=70)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_joined', models.DateField()),
            ],
        ),
    ]
