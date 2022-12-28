from rest_framework import serializers

from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    class Meta:

        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:

        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)


class SensorDetailsSerializer(serializers.ModelSerializer):

    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:

        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


