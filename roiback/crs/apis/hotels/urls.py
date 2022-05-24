from django.urls import include, path
from .views import HotelView, HotelSingleViews
# from roiback.crs.apis.hotels.views import views

urlpatterns = [
    path('', HotelView.as_view()),
    path('<str:code>/', HotelSingleViews.as_view()),
]