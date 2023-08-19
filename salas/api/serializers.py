from rest_framework import serializers

from salas.models import Sala

class SalaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = "__all__"