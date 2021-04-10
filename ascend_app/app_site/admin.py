from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


admin.site.register(Student)
admin.site.register(Recruiter)
admin.site.register(Company)
admin.site.register(Competition)
