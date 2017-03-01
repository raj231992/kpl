from django.conf.urls import url
from .views import Match_Display
urlpatterns = [
    url(r'^schedule/$', Match_Display.as_view(),name='schedule'),
]