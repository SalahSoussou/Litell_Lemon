from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.bookingview.as_view()),
    path('menu/', views.menuview.as_view()),

    # path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
]
