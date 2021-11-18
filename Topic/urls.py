"""learningLog URL Configuration

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
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/', views.topic, name='topic'),
    path('topic/<int:topic_id>', views.entry, name='entry'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('addEtry/<int:topic_id>', views.addEntry, name='addEntry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
    path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
    path('subscribe', views.subscribe, name='subscribe'),
]
