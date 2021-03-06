# Generated by Django 2.2.1 on 2019-05-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=70)),
                ('phone_number', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=100)),
                ('date_joined', models.DateField()),
                ('subject_training', models.CharField(max_length=40)),
                ('number_of_subjects', models.CharField(max_length=10)),
            ],
        ),
    ]
