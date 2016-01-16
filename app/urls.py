from django.conf.urls import patterns, include, url

from .views import IndexView, SetupView

app_name = 'app'
urlpatterns = [
    url('^setup/?$', SetupView.as_view(), name='setup'),
    url('^$', IndexView.as_view(), name='index'),
]
