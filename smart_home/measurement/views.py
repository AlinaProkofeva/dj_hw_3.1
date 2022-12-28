# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.serializers import SensorSerializer, MeasurementSerializer, Measurement, SensorDetailsSerializer
from measurement.models import Sensor, Measurement


class SensorsAPIView(ListAPIView):
    '''
    Отображение информации обо всех датчиках
    '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        '''
        Создание нового датчика
        '''
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class MeasureAPIView(ListAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        '''
        Добавление измерения температуры по ID датчика
        '''
        serializer = MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class SensorMeasurementsAPIView(ListAPIView):
    '''
    В процессе((
    '''
    queryset = Sensor.objects.filter(id=1)
    serializer_class = SensorDetailsSerializer

    def put(self, request, *args, **kwargs):
        '''
        Изменение информации о датчике
        '''
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': 'Method PUT not allowed'})

        try:
            instance = Sensor.objects.get(pk=pk)
        except:
            return Response({'Error': 'Object does not exist'})

        serializer = SensorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        '''
        удаление датчика
        '''
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': 'Method DELETE not allowed'})
        Sensor.objects.filter(id=pk).delete()
        return Response('Deleted sensor id ' + str(pk))