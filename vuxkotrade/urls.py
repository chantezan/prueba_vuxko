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

from django.contrib.auth.models import User

# Create user and save to the database
try:
    print("try ecreando")
    go = User.objects.get(username='user2')
except User.DoesNotExist:
    print("ecreando")
    user = User.objects.create_user('user2', 'use2r@crazymail.com', 'user2')
    # Update fields and then save again
    user.first_name = 'user2'
    user.last_name = 'user2'
    user.save()


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
