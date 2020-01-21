from django.urls import path, re_path
from shop import views
from django.urls import register_converter
from . import views
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year, name='archives_year'),
    path('', views.item_list, name='item_list'),
    #path('ddd/', views.response_pillow_image),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    # re_path(r'^(?P<pk>\d+)/$', views.item_detail)
    path('new/', views.item_new, name='item_new'),
    path('<int:pk>/edit', views.item_edit, name='item_edit'),
]