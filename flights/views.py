from rest_framework.generics import ListAPIView
from .models import Booking, Flight
from .serializers import ListSerializer, BookingListView
from datetime import datetime

class ListofFligth(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

class ListofBooking(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListView
