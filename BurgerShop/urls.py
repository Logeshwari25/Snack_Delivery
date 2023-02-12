"""BurgerShop URL Configuration

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
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.before_home),
    path('homepage',views.home),

    path('signup',views.signup),
    path('login_usr',views.login_usr),
    path('create_user',views.create_user),

    path('view_order',views.view_order),
    path('make_order',views.make_order),

    path('list_blog',views.list_blog),
    path('list_edit_blog',views.list_edit_blog),
    path('view_blog/<str:pk>',views.view_blog),
    path('edit_blog/<str:pk>',views.edit_blog),
    path('blog_edit',views.blog_edit),
    path('save_blog',views.save_blog),
    path('delete_blog',views.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',views.save_edit_blog),

]
