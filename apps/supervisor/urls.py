from django.urls import path
from . import views

app_name = 'supervisor'

urlpatterns = [
    path('load-average/',
         views.load_average,
         name='load-average'),

    path('ram/',
         views.ram,
         name='ram'),
]
