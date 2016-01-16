from django.conf.urls import patterns, include, url

from .views import IndexView, SetupView

urlpatterns = [
    url('^setup/?$', SetupView.as_view()),
    url('^$', IndexView.as_view()),
]
