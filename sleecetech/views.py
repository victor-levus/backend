from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from sleecetech.models import Message
from sleecetech.serializer import SleeceMessageSerializer

# Create your views here.

requestType = ('POST')

class SleeceMessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = SleeceMessageSerializer

    def get_permissions(self):
        if self.request.method in requestType:
            return [AllowAny()]
        return [IsAuthenticated()]