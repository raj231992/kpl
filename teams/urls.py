from django.conf.urls import url
from .views import Team_Display

urlpatterns = [
    url(r'^$', Team_Display.as_view()),
]