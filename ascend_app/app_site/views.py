import datetime
from urllib.parse import urlencode

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from .models import *
from twilio.rest import Client
from django.contrib.auth import authenticate, login


def index(request):
    data = []
    persons = [AuthUser.objects.all()]
    companies = [Company.objects.all()]
    data_to_display = False
    if len(persons) > 0 or len(companies) > 0:
        data_to_display = True
    template = 'app_site/index.html'
    context = {
        'data_to_display': data_to_display,
        'persons': persons,
        'companies': companies,
    }
    return render(request, template, context)


def about_student(request):
    template = loader.get_template('app_site/about_student.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def about_company(request):
    template = loader.get_template('app_site/about_company.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def login_page(request):
    form = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Successful login
            # messages.success(request, 'Login was Successful!') TODO does this work?
            # base_url = reverse('student_portal')  # 1 /student/portal/
            # query_string = urlencode({'auth': user})  # 2 category=42
            # url = '{}?{}'.format(base_url, query_string)  # 3 /products/?category=42
            return redirect('student/portal/')
        else:
            # Unsuccessful Login
            form = LoginForm()
            messages.success(request, 'Failed to login. Check your credentials and try again.')
    else:
        form = LoginForm()
    template = 'app_site/welcome_student.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def register(request):
    template = loader.get_template('app_site/register.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def student_portal(request):
    if not request.user.is_authenticated:
        return redirect('/')  # TODO show error page for auth
    else:
        template = loader.get_template('app_site/student_portal.html')
        context = {
            'data': '123',
        }
        return HttpResponse(template.render(context, request))


def company_portal(request):
    if not request.user.is_authenticated:
        return redirect('/')  # TODO show error page for auth
    else:
        template = loader.get_template('app_site/company_portal.html')
        context = {
            'data': '123',
        }
        return HttpResponse(template.render(context, request))


def welcome_student(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            user, password, first, last, email, phone, gender = get_person_data_form(form)
            study = form.cleaned_data['study']
            searching = form.cleaned_data['currently_searching']
            new_student = AuthUser(username=user, password=password, first_name=first, last_name=last, email=email,
                                   phone_number=phone, gender=gender, study=study, currently_searching=searching)
            # Authenticate new user
            user_exists = authenticate(request, username=user, password=password)
            if user_exists is not None:
                login(request, user_exists)
                # account_sid = 'AC9804d93a0f1cdd98f902a7795c974ab5'
                # auth_token = 'aa6300062f8d21a8afe97c35799cf332'
                # client = Client(account_sid, auth_token)
                # client.api.account.messages.create(
                #     to="+14806656001",
                #     from_="+12512999273",
                #     body="New person created!\n"
                #          f"{first} {last},\n"
                #          f"contact: {phone} {email}\n"
                #          f"date: {datetime.datetime.now()}\n"
                #          f"info: {study}\n")
                messages.success(request, 'Register was Successful!')
                return redirect('student/portal/')
            else:
                raise Exception('Something strange happened here.')
    else:
        form = PersonForm()
    template = 'app_site/welcome_student.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def welcome_company(request):
    if request.method == 'POST':
        message = ''
        company_form = None
        recruiter_form = None
        print(request.POST)
        if 'company_name' in request.POST:
            print('Company Form')
            company_form = CompanyForm(request.POST)
            recruiter_form = RecruiterForm()
            if company_form.is_valid():
                name = company_form.cleaned_data['company_name']
                phone = company_form.cleaned_data['phone_number']
                company = Company(company_name=name, phone_number=phone)
                company.save()
                message = 'Company successfully registered!'
                messages.success(request, message)
        elif 'username' in request.POST:
            print('Recruit Form')
            recruiter_form = RecruiterForm(request.POST)
            company_form = CompanyForm()
            if recruiter_form.is_valid():
                user, password, first, last, email, phone, gender = get_person_data_form(recruiter_form)
                company = recruiter_form.cleaned_data['associated_company']
                recruiter = AuthUser(username=user, password=password, first_name=first, last_name=last, email=email,
                                      phone_number=phone, gender=gender, associated_company=company, is_student=False)
                recruiter.save()
                message = 'Recruiter successfully registered!'
                messages.success(request, message)
                return redirect('/company/portal/', recruiter.id)
    else:
        recruiter_form = RecruiterForm()
        company_form = CompanyForm()
    template = 'app_site/welcome_company.html'
    context = {
        'company_form': company_form,
        'recruiter_form': recruiter_form,
    }
    return render(request, template, context)


def get_person_data_form(form):
    user = form.cleaned_data['username']
    password = form.cleaned_data['password']
    first = form.cleaned_data['first_name']
    last = form.cleaned_data['last_name']
    email = form.cleaned_data['email']
    phone = form.cleaned_data['phone_number']
    gender = form.cleaned_data['gender']
    return user, password, first, last, email, phone, gender


def competition_gallery(request):
    template = loader.get_template('app_site/competition_gallery.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def competition_detail(request, competition_id):
    template = loader.get_template('app_site/competition_detail.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def create_competition(request, competition_id):
    template = loader.get_template('app_site/create_competition.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))
