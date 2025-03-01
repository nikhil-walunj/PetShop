from rest_framework import serializers
from .models import custForm

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=custForm
        fields='__all__'



