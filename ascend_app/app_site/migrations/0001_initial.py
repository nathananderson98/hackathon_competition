# Generated by Django 3.1.5 on 2021-04-10 17:09

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_type', models.CharField(choices=[('dev', 'Software Development'), ('gov', 'Government'), ('fin', 'Finance'), ('cos', 'Consulting'), ('ent', 'Entrepreneur'), ('adv', 'Advertising'), ('gde', 'Graphic Design'), ('ani', 'Animation'), ('dsi', 'Data Science'), ('cju', 'Criminal Justice'), ('ecn', 'Economics'), ('con', 'Conservation'), ('ide', 'Interior Design'), (None, 'Undecided')], default=None, max_length=3)),
                ('date_launch', models.DateTimeField()),
                ('date_close', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message="Username must be 6 to 20 characters long and can't contain any of the following: '.' or '_' at the beginning or end, '..', '._', '_.', or '__'", regex='^(?=.{6,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')])),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Password must be a minimum of eight character and contain at least one upper-case letter and one number', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d\\w\\W]{8,}$')])),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='m', max_length=1)),
                ('is_student', models.BooleanField(default=True)),
                ('study', models.CharField(choices=[('dev', 'Software Development'), ('gov', 'Government'), ('fin', 'Finance'), ('cos', 'Consulting'), ('ent', 'Entrepreneur'), ('adv', 'Advertising'), ('gde', 'Graphic Design'), ('ani', 'Animation'), ('dsi', 'Data Science'), ('cju', 'Criminal Justice'), ('ecn', 'Economics'), ('con', 'Conservation'), ('ide', 'Interior Design'), (None, 'Undecided')], default='Undecided', max_length=3, verbose_name='Field of Study')),
                ('currently_searching', models.BooleanField(default=True, verbose_name='Search for a Job?')),
                ('associated_company', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='app_site.company')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]