from django.contrib.auth.models import User
from django.db import models
import datetime
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

STUDY_CHOICES = [
    ('dev', 'Software Development'),
    ('gov', 'Government'),
    ('fin', 'Finance'),
    ('cos', 'Consulting'),
    ('ent', 'Entrepreneur'),
    ('adv', 'Advertising'),
    ('gde', 'Graphic Design'),
    ('ani', 'Animation'),
    ('dsi', 'Data Science'),
    ('cju', 'Criminal Justice'),
    ('ecn', 'Economics'),
    ('con', 'Conservation'),
    ('ide', 'Interior Design'),
    (None, 'Undecided'),
]



class Student(models.Model):
    first_name = models.CharField("First Name", max_length=20)
    last_name = models.CharField("Last Name", max_length=30)
    email = models.EmailField(max_length=254)
    username_regex = RegexValidator(regex='^(?=.{6,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',
                                    message="Username must be 6 to 20 characters long and can\'t contain any of the "
                                            "following: '.' or '_' at the beginning or end, '..', '._', '_.', or '__'")
    username = models.CharField(unique=True, validators=[username_regex], max_length=20)
    password_regex = RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\w\W]{8,}$',
                                    message="Password must be a minimum of eight character and contain at least one "
                                            "upper-case letter and one number")
    password = models.CharField(validators=[password_regex], max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(unique=True, validators=[phone_regex], max_length=17, blank=True)
    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default='m')
    study = models.CharField("Field of Study", choices=STUDY_CHOICES, max_length=3, default='Undecided')
    # participated_competitions = models.
    currently_searching = models.BooleanField("Search for a Job?", default=True)


class Recruiter(models.Model):
    first_name = models.CharField("First Name", max_length=20)
    last_name = models.CharField("Last Name", max_length=30)
    email = models.EmailField(max_length=254)
    username_regex = RegexValidator(regex='^(?=.{6,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$',
                                    message="Username must be 6 to 20 characters long and can\'t contain any of the "
                                            "following: '.' or '_' at the beginning or end, '..', '._', '_.', or '__'")
    username = models.CharField(unique=True, validators=[username_regex], max_length=20)
    password_regex = RegexValidator(regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\w\W]{8,}$',
                                    message="Password must be a minimum of eight character and contain at least one "
                                            "upper-case letter and one number")
    password = models.CharField(validators=[password_regex], max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(unique=True, validators=[phone_regex], max_length=17, blank=True)
    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default='m')
    associated_company = models.ForeignKey('Company', on_delete=models.CASCADE)


class Company(models.Model):
    company_name = models.CharField(max_length=30, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone_number = models.CharField(unique=True, validators=[phone_regex], max_length=17, blank=True)
    # address = AddressField() FIXME not importing address.models properly but installed with pip

    def __str__(self):
        return self.company_name


class LoginStudent(ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']


class LoginRecruiter(ModelForm):
    class Meta:
        model = Recruiter
        fields = ['username', 'password']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'gender', 'study',
                  'currently_searching']


class RecruiterForm(ModelForm):
    class Meta:
        model = Recruiter
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'gender',
                  'associated_company']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'phone_number']


class Competition(models.Model):
    comp_type = models.CharField(choices=STUDY_CHOICES, max_length=3, default=None)
    date_launch = models.DateTimeField()
    date_close = models.DateTimeField()
    # selected_winners = models.ForeignKey('User', on_delete=models.CASCADE) FIXME get a list of users

    def __str__(self):
        return f'{self.comp_type} : Start - {self.date_launch} | Close - {self.date_close}'

    def is_open(self):
        return self.date_close < timezone.now()
