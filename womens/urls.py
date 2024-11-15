"""womens URL Configuration

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
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('',views.index),
    path('reg/',views.signup),
    path('login/',views.login),
    path('forgot/',views.forgotpassword),
    path('uhome/',views.uhome),
    path('upload_status/',views.upload_status),
    path('addmultiple/',views.addmultiple),
    path('getstatusdata/',views.getstatusdata),
    path('profile/',views.profile),
    path('about/',views.about),
    path('gallery/',views.gallery),
    path('viewprofile/',views.viewprofile),
    path('addfriend/',views.addfriend),
    path('requestlist/',views.requestlist),
    path('action/',views.action),
    path('message/',views.message),
    path('viewstatus/',views.viewstatus),
    path('addlike/',views.addlike),
    path('reportstatus/',views.statusreport),
    path('addcomplaints/',views.addcomplaints),
    path('ahome/',views.ahome),
    path('viewcomplaints/',views.viewcomplaints),
    path('viewstatusreport/',views.viewstatusreport),
    path('viewmessagereport/',views.viewmessagereport),
    path('admin_change_block/',views.admin_change_block),
    path('friends/',views.friends),

]

