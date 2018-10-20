"""eRPMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^js_register/$',views.js_register),
    url(r'^js_login/$',views.js_login),
    url(r'^js_view_jobs/$',views.js_view_jobs),
    url(r'^js_dashboard/$',views.js_dashboard),
    url(r'^js_profile_edit/$',views.js_profile_edit),
    url(r'^js_online_exam_registration/$',views.js_online_exam_registration),
    url(r'^comp_registration/$',views.comp_registration),
    url(r'^comp_login/$',views.comp_login),
    url(r'^comp_dashboard/$',views.comp_dashboard),
    url(r'^comp_profile_edit/$',views.comp_profile_edit),
    url(r'^comp_post_jobs/$',views.post_jobs),
    url(r'^comp_view_jobs/$',views.view_jobs),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^dashboard/$',views.dashboard),
    url(r'^delete/$',views.delete),
    url(r'^view_all_company/$',views.view_all_company),
    url(r'^view_all_jobseeker/$',views.view_all_jobseeker),
    url(r'^view_all_jobs/$',views.view_all_jobs),
    path('admin/', admin.site.urls),
]
