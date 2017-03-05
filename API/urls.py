from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from API import views

urlpatterns = [
    url(r'^words/$', views.WordList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)