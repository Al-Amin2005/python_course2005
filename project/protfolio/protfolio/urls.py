"""
URL configuration for protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
    # path('admin/', admin.site.urls),

    path('',views.demo),
    path('subpath1',views.demo1),
    path('admin/about',views.about_index,name = 'about'),
    path('admin/about/insert',views.about_insert, name='about_insert'),
    path('admin/edit/<int:id>',views.edit_index,name = 'edit_index'),
    path('admin/edit',views.about_edit,name='about_edit'),
    path('admin/delete/<int:id>',views.delete_index,name = 'delete_index')
]
