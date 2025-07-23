from django.urls import path
from . import views
from .views import MenuItemView, SingleMenuItemView, MenuItemDetailView



urlpatterns = [
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api/menu-items/<int:pk>/', views.MenuItemDetailView.as_view()),

    
]
