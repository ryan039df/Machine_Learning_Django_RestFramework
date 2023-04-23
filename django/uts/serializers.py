from rest_framework import serializers
from .models import Sensor, Sensor2, Sensor3, Actuator
    
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"


class SensorSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Sensor2
        fields = "__all__"
    

class SensorSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Sensor3
        fields = "__all__"


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = "__all__"