# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailsSerializer
from measurement.models import Sensor, Measurement


class SensorsAPIView(ListCreateAPIView):
    '''
    * Отображение информации обо всех датчиках
    * Создание нового датчика
    '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasureAPIView(ListCreateAPIView):
    '''
    * Добавление измерения температуры по ID датчика
    * Просмотр списка измерений
    '''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorMeasurementsAPIView(RetrieveUpdateDestroyAPIView):
    '''
    * Изменение информации о датчике
    * Удаление датчика
    * Полная информация по датчику со всеми измерениями
    '''
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer



