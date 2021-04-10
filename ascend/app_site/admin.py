from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


admin.site.register(AuthUser, UserAdmin)
admin.site.register(Person)
admin.site.register(Recruiter)
admin.site.register(Company)
admin.site.register(Competition)
