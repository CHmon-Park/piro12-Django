from django.urls import path, re_path
from shop import views
from django.urls import register_converter
from . import views
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    #path('ddd/', views.response_pillow_image),
]