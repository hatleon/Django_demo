"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
    3.博客入门 http://www.liujiangblog.com/blog/36/ jquery+bootstrap+form+action sqlit3数据库
    4. https://blog.csdn.net/qq_19339041/article/details/79721696 form表单提交
    5. 运行python manage.py runserver 或 python manage.py runserver 127.0.0.1:8000
"""
from django.contrib import admin
from django.urls import path
from booktest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('test/', views.test),
]
