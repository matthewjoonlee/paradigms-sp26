from django.urls import path
from polls.views import home
urlpatterns = [
    path("", home, name="home"),
]