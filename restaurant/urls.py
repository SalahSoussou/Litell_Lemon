from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('home/', views.home),
    path('menu/', views.MenuItemViw.as_view()),
    path('menu/<int:pk>', views.SinglMenuItemViw.as_view()),
    path('api-token-auth/', obtain_auth_token),

]
