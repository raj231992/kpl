from django.conf.urls import url
from .views import Team_Display,Team_Players

urlpatterns = [
    url(r'^$', Team_Display.as_view(),name='display'),
    url(r'^players/(?P<pk>[0-9]+)/', Team_Players.as_view(),name='players'),
]