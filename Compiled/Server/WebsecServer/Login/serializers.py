from rest_framework import serializers
from .models import ModelsActiveStatus

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsActiveStatus
        fields = ('username', 'statusString')
        #fields = '__all__'