"""earlybirds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import landing.views as views
from django.contrib.auth.views import LogoutView
from .settings import LOGOUT_REDIRECT_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='landing'),
    path('internships', views.internships, name='internships'),
    path('courses', views.courses, name='courses'),
    path('projects', views.projects, name='projects'),
    path('profile', views.profile, name='profile'),
    path('skill_detail', views.skill_detail, name='skill_detail'),
    path('team', views.team, name='team'),
    path('signup', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path('courses/1', views.course_detail, name='course_detail'),
    path('projects/1', views.project_detail, name='project_detail'),
]
