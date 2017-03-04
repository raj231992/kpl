from django.conf.urls import url
from .views import Home,Rules,Register,Organizers,Players,Match_Details
urlpatterns = [
    url(r'^$', Home.as_view(),name='home'),
    url(r'^rules/$', Rules.as_view(),name='rules'),
    url(r'^organizers/$', Organizers.as_view(),name='organizers'),
    url(r'^players/$', Players.as_view(),name='players'),
    url(r'^match_details/(?P<match>[0-9]+)/$', Match_Details.as_view(),name='match_details'),
]