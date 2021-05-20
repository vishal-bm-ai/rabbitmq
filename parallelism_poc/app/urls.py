from django.urls import path, include
from .views import GenerateJobView, Process


urlpatterns = [
    path('',Process.as_view(),name='job'),
]