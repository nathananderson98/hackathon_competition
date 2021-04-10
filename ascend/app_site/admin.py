from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Recruiter)
admin.site.register(Company)
admin.site.register(Competition)
