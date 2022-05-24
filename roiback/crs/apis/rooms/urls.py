from django.urls import path
from .views import RoomView, RoomSingleViews, RoomHotelViews, RoomFullView

urlpatterns = [
    path('', RoomView.as_view()),
    path('<str:code>/', RoomSingleViews.as_view()),
    path('hotel/<str:code>/', RoomHotelViews.as_view()),
    path('<str:code>/inventory/', RoomFullView.as_view()),
]