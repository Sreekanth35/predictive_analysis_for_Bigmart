# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('download_excel/', views.download_excel, name='download_excel'),
]
