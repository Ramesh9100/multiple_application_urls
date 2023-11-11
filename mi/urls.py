from mi.views import *

from django.urls import path

app_name='Nothing'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumra/',bumra,name='bumra'),
]