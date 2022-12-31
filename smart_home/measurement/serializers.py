from rest_framework import serializers

from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class MeasurementSensorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailsSerializer(serializers.ModelSerializer):

    measurements = MeasurementSensorSerializer(read_only=True, many=True)

    class Meta:

        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']




