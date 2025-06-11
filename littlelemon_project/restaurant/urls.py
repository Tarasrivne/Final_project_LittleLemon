from django.urls import path
from . import views
from .views import MenuItemView, SingleMenuItemView


urlpatterns = [
    path('menu/items', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
