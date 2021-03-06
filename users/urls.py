"""Defines URLs for users"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Login Page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),

    # Registration page
    url(r'^register/$', views.register, name='register'),

    # logout page
    url(r'^logout/$', views.logout_view, name='logout'),
]