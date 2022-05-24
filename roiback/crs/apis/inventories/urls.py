from django.urls import path
from .views import InventoryView, InventorySingleViews, InventoriesRateViews

urlpatterns = [
    path('', InventoryView.as_view()),
    # path('<str:code>/', InventorySingleViews.as_view()),
    path('rate/<str:code>/<str:date>', InventorySingleViews.as_view()),
    path('rate/<str:code>/', InventoriesRateViews.as_view()),
    # path('room/<str:code>/', InventoriesRoomViews.as_view()),
]