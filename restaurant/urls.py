from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.bookingview.as_view()),
    path('m/', views.menuview.as_view()),
    path('s/', views.msg),
    path('menu/', views.MenuItemViw.as_view()),
    path('menu/<int:pk>', views.SinglMenuItemViw.as_view()),
    # path('', views.home, name="home"),
    # path('about/', views.about, name="about"),
]
