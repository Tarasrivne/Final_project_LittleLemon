from rest_framework import generics
from rest_framework.decorators import api_view
from .models import MenuItem
from .models import Booking
from .serializers import MenuItemSerializer
from .serializers import BookingSerializer

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer