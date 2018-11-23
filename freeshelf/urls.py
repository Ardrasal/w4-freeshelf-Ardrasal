"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView
from freeshelf import views

urlpatterns = [
    path('', views.index, name='home'),
    path('favorites/', TemplateView.as_view(template_name='favorites.html'),
         name='favorites'),
    path('category/', TemplateView.as_view(template_name='category.html'),
         name='category'),
    path('books/<slug>/', views.book_detail, name='book_detail'),
    path('admin/', admin.site.urls),
]
