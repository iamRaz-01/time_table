from django.urls import path
from .views import timetable




urlpatterns = [
    path('', timetable, name='timetable'),
]

