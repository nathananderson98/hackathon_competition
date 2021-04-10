from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('about/student/', views.about_student, name='about_student'),

    path('about/company/', views.about_company, name='about_company'),

    path('login/', views.login_page, name='login'),

    path('register/', views.register, name='register'),

    path('student/portal/', views.student_portal, name='student_portal'),

    path('company/portal/', views.company_portal, name='company_portal'),

    path('welcome/student/', views.welcome_student, name='welcome_student'),

    path('welcome/company/', views.welcome_company, name='welcome_company'),

    path('competitions/', views.competition_gallery, name='competition_gallery'),

    path('competitions/<int:pk>/', views.competition_detail, name='competition_detail'),

    path('competitions/create/', views.create_competition, name='create_competition'),

]
