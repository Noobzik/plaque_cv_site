from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", views.vehicules, name="vehicules"),
    path("camera/", views.webcam, name='webcam1'),
    path("feed/", views.feed, name='webcam1')
]
