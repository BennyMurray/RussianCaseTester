
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from API import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('API.urls')),
]
