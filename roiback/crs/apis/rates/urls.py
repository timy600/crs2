from django.urls import path
from .views import RateView, RateSingleViews, RatesRoomViews

urlpatterns = [
    path('', RateView.as_view()),
    path('<str:code>/', RateSingleViews.as_view()),
    path('room/<str:code>/', RatesRoomViews.as_view()),
]