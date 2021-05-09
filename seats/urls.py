from django.urls import path

from .views import SeatsView, AttendanceView

urlpatterns = [
    path('', SeatsView.as_view(), name='seats'),
    path('attend', AttendanceView.as_view(), name='attend')
]
