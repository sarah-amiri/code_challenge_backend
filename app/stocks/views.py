import datetime

from django.core import cache
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from stocks.models import BuyingStock
from stocks.serializers import BuyingStockSerializer, BuyStockBodySerializer


class BuyStockAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = BuyingStock.objects.filter(
            Q(creation_date__date=datetime.date.today()) | Q(status=BuyingStock.ACCEPTED))
        queryset = queryset.exclude(quantity__lt=10, status=BuyingStock.DENY)
        queryset = queryset.order_by('-creation_date')
        serializer = BuyingStockSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BuyStockBodySerializer(data=request.data)
        if serializer.is_valid():
            user_credit = cache.get(request.data['user'], {}).get('credit', None)
            stocks = cache.get(request.data['stock'], None)
            if user_credit is None or stocks is None:
                return Response(dict(message='Deny'), status=HTTP_404_NOT_FOUND)

            user_credit, stock_price = int(user_credit), int(stocks['price'][-1])
            quantity = int(request.data['quantity'])
            data = request.data.copy()
            data['price'] = stock_price
            if user_credit < (quantity * stock_price) or quantity <= 0:
                data.update({'status': BuyingStock.DENY})
                serializer = BuyingStockSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(dict(message='Deny'), status=HTTP_400_BAD_REQUEST)
            data.update({'status': BuyingStock.ACCEPTED})
            serializer = BuyingStockSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(dict(message='Accept'), status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
