"""
URL configuration for SKZ_Billing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from SKZ_Billing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.welcome ),
    path('home', views.home),
    path('about-us', views.aboutus),
    path('services', views.services),
    path('services/rcm', views.rcm),
    path('services/credentialing', views.credentialing),
    path('services/medical-coding', views.medical_coding),
    path('services/billing', views.billing),
    path('services/compliance-report', views.compliance_report),
    path('services/dental', views.dental),
    path('contact', views.contact_view),
    path('contact/appointment-request',views.appointment_request),
    path('privacy-policy',views.privacy_policy),


    path("__reload__/", include("django_browser_reload.urls")),
]
