from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    # path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
]
