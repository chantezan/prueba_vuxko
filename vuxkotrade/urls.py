"""rateteams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from tradeapp import views



# Create user and save to the database


urlpatterns = [
    path('loginuser/', views.loginUser),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('bot', views.getBot),
    path('botsave', views.saveBot),
    path('getema', views.getEma),
    path('seebot/<int:see_bot>', views.SeeBot),
    path('getonebot/<int:see_bot>', views.GetOneBot),
    path('checkentrada/<int:see_bot>', views.CheckEntrada),
]
