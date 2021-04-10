# Generated by Django 3.2 on 2021-04-10 04:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_launch', models.DateTimeField()),
                ('date_close', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Username must be 8 to 20 characters long and can't contain any of thefollowing: '.' or '_' at the beginning or end, '..', '._', '_.', or '__'", regex='^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')])),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Password must be a minimum of eight character and contain at least one letter and one number', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d\\w\\W]{8,}$')])),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='m', max_length=1)),
                ('study', models.CharField(choices=[('dev', 'Software Development'), ('gov', 'Government'), ('fin', 'Finance'), ('cos', 'Consulting'), ('ent', 'Entrepreneur'), ('adv', 'Advertising'), ('gde', 'Graphic Design'), ('ani', 'Animation'), ('dsi', 'Data Science'), ('cju', 'Criminal Justice'), ('ecn', 'Economics'), ('con', 'Conservation'), ('ide', 'Interior Design'), (None, 'Undecided')], default=None, max_length=3)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('currently_searching', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Username must be 8 to 20 characters long and can't contain any of thefollowing: '.' or '_' at the beginning or end, '..', '._', '_.', or '__'", regex='^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')])),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Password must be a minimum of eight character and contain at least one letter and one number', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d\\w\\W]{8,}$')])),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='m', max_length=1)),
                ('associated_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_site.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]