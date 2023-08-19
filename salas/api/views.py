from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from salas.api.serializers import SalaSerializers

from salas.models import Sala

class SalaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = SalaSerializers
    queryset = Sala.objects.all()
    http_method_names = ['get','post']
