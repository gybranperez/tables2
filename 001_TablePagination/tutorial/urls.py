"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from tutorial import views
from tutorial.views import PersonListView,PersonTableView,PersonTableFunction
from django_filters.views import FilterView
urlpatterns = [
    path('', views.index, name='index'),  # Acá,
    #path('', IndexTable.as_view(), name='index'),  # Acá,
    path("peopleList/", PersonListView.as_view(), name='peoplelist'),
    path("peopleTable/", PersonTableView.as_view(),name='peopletable'),
    path('peopleTableFunction/', views.PersonTableFunction, name='peopletablefunction'), 
]
