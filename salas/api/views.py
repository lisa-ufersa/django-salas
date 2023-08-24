from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from salas.api.serializers import SalaSerializers

from salas.models import Sala

class SalaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalaSerializers
    queryset = Sala.objects.all()

