from rest_framework.generics import ListAPIView
from .models import Booking, Flight
from .serializers import ListSerializer

class ListofFligth(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

