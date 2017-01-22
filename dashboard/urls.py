from django.conf.urls import url
from .views import Home,Rules,Register,Organizers
urlpatterns = [
    url(r'^$', Home.as_view(),name='home'),
    url(r'^rules/$', Rules.as_view(),name='rules'),
    url(r'^register/$', Register.as_view(),name='register'),
    url(r'^organizers/$', Organizers.as_view(),name='organizers'),
]