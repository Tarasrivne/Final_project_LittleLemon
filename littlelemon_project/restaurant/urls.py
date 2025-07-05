from django.urls import path
from . import views
from .views import MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-auth-token', obtain_auth_token),
]
