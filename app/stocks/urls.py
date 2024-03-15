from django.urls import path

from stocks.views import BuyStockSerializer

urlpatterns = [
    path('', BuyStockSerializer.as_view(), name='buy-stocks'),
]
