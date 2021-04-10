import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *
from twilio.rest import Client


def index(request):
    data = []
    data.append(User.objects.all())
    data.append(Recruiter.objects.all())
    data.append(Company.objects.all())
    data_to_display = False
    if len(data) > 0:
        data_to_display = True
    template = loader.get_template('app_site/index.html')
    context = {
        'data_to_display': data_to_display,
        'data': data,
    }
    return HttpResponse(template.render(context, request))


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


def login(request):
    template = loader.get_template('app_site/login.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('app_site/register.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def student_portal(request, student):
    template = loader.get_template('app_site/student_portal.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def company_portal(request, company):
    template = loader.get_template('app_site/company_portal.html')
    context = {
        'data': '123',
    }
    return HttpResponse(template.render(context, request))


def welcome_student(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user, password, first, last, email, phone, gender = get_person_data_form(form)
            study = form.cleaned_data['study']
            searching = form.cleaned_data['searching']
            user = User(username=user, password=password, first_name=first, last_name=last, email=email,
                        phone_number=phone, gender=gender, study=study, searching=searching)
            user.save()
            account_sid = 'AC9804d93a0f1cdd98f902a7795c974ab5'
            auth_token = 'aa6300062f8d21a8afe97c35799cf332'
            client = Client(account_sid, auth_token)
            client.api.account.messages.create(
                to="+14806656001",
                from_="+12512999273",
                body="New person created!\n"
                     f"{first} {last},\n"
                     f"contact: {phone} {email}\n"
                     f"date: {datetime.datetime.now()}\n"
                     f"info: {study}\n")
            messages.success(request, 'Register was Successful!')
    else:
        form = UserForm()
    template = 'app_site/welcome_student.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def welcome_company(request):
    if request.method == 'POST':
        message = ''
        if 'Register Company' in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                name = company_form.cleaned_data['company_name']
                company = Company(company_name=name)
                company.save()
                message = 'Company successfully registered!'
        elif 'Register Recruiter' in request.POST:
            recruiter_form = RecruiterForm(request.POST)
            if recruiter_form.is_valid():
                user, password, first, last, email, phone, gender = get_person_data_form(recruiter_form)
                company = recruiter_form.cleaned_data['company']
                recruiter = Recruiter(username=user, password=password, first_name=first, last_name=last, email=email,
                                      phone_number=phone, gender=gender, associated_company=company)
                recruiter.save()
                message = 'Recruiter successfully registered!'
            messages.success(request, message)
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
