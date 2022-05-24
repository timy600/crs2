from django.urls import path
from .views import AvailabilityView

urlpatterns = [
    path('<str:code>/<str:checkin_date>/<str:checkout_date>/', AvailabilityView.as_view()),
]