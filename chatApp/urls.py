"""chatApp URL Configuration

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
from . import views as base_views

from .import views

from chat import views as chat_views

from accounts import urls as accounts_urls
from chat import urls as chat_urls

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.HomePage.as_view(), name='home'),
    path('accounts/', include(accounts_urls)),
    path('chat/', include(chat_urls)),
    path('detection/', views.DETECTION_PAGE, name='detection'), 
    path('display_result', views.display_result, name = 'display_result'),
    path('feedback', views.feedback, name = 'feedback'),
    path('disease_description', views.disease_description, name = 'disease_description'),
    path('crop_description', views.crop_description, name = 'crop_description'),
    path('crop_details/<str:crop_name>/', views.crop_details, name='crop_details'),

]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

