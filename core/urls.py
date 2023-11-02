from django.urls import path
from .views import home, add_music

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("add", add_music, name="add"),
]