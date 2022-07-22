"""Project_Final URL Configuration

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
from dangnhap import views

urlpatterns = [
 path('', views.dangnhap),
 path('xuly_dangnhap/', views.xuly_dangnhap, name="xuly_dangnhap") ,
 path('xuly_capnhat/', views.xuly_capnhat, name="xuly_capnhat") ,
 path('chitiet/<int:nguoidung_id>/', views.chi_tiet, name="chi_tiet") ,
 path('xoa/<int:nguoidung_id>/', views.xoa_nguoidung, name="xoa_nguoidung") ,
]
