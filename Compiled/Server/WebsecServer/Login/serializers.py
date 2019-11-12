from rest_framework import serializers
from .models import ModelsActiveStatus, Logs

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsActiveStatus
        fields = ('username', 'statusString')
        #fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('username','site', 'status')