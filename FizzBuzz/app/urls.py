from django.urls import path
from .views import FizzBuzzView

urlpatterns = [
    path('',FizzBuzzView.as_view(), name='home')
]
