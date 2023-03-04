from rest_framework.generics import ListAPIView 
from .models import Booking, Flight
from .serializers import FlightListSerializer, BookingLisSerializer
from django.utils import timezone


class ListofFligth(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class ListofBooking(ListAPIView):
    queryset = Booking.objects.filter(date__gte=timezone.now())
    serializer_class = BookingLisSerializer
