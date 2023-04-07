"""reservationApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path("logout", index.LOGOUT,name='logout'),
    path("", index.SINGIN,name='login'),
    path("admin/", admin.site.urls),
    path('recuperation', index.recuperation,name='dashbord'),
    path('', index.connection,name='connection'),
    path('register', index.REGISTER,name='register'),
    path('dashbord', index.dashbord,name='dashbord'),
    path('code_recuperation', index.code,name='code_recuperation'),
    path('reservation', index.Reservation,name='reservation'),
    path('service', index.Service,name='service'),
    path('residence', index.Residence,name='residence'),
    path('gestion', index.Gestion,name='gestion'),
    path('client', index.Client,name='client'),
    path('recuperation', index.Recuperation,name='recuperation'),
]

urlpatterns += staticfiles_urlpatterns()
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
