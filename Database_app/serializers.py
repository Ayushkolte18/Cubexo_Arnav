from rest_framework import serializers
from .Database import records

class Myserializers(serializers.Serializer):

    class Meta:
        records = records
        fields = '__all__'