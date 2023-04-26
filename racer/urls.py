from django.urls import path
from . import views

urlpatterns = [
    path('add_race_time/', views.add_race_time, name='add_race_time'),
    path('view_race_time/', views.race_time_list, name='race_time_list'),
]
