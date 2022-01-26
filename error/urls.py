"""text_utilities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

#self-editted
from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.index, name='index'),
    # path ('about', views.about, name='about'),       #run this by typing /about with address of http
    # path ('remove_punctuation', views.remove_punctuation, name='remove_punctuation'),
    # path ('CapFirst', views.CapFirst, name='CapFirst'),
    # path ('NewLineRemover', views.NewLineRemover, name='NewLineRemover'),
    # path ('SpaceRemover', views.SpaceRemover, name='SpaceRemover'),
    # path ('CharCount', views.CharCount, name='CharCount'),
    path ('Analyze', views.Analyze, name='Analyze'),
]
