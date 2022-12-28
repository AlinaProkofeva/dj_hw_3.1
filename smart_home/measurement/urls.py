from django.urls import path
from measurement.views import SensorsAPIView, SensorMeasurementsAPIView, MeasureAPIView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('sensors/', SensorsAPIView.as_view()),
    path('sensors/<pk>/', SensorMeasurementsAPIView.as_view()),
    path('measures/', MeasureAPIView.as_view()),

]
