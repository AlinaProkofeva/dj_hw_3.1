from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    description = models.CharField(max_length=150, null=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, related_name='measurements')
    temperature = models.DecimalField(max_digits=10, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

