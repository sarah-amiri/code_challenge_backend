from django.core import cache
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from stocks.serializers import BuyStockSerializer


class BuyStockAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BuyStockSerializer(data=request.data)
        if serializer.is_valid():
            user_credit = cache.get(request.data['user'], {}).get('credit', None)
            if user_credit is None:
                return Response(dict(message='Deny'), status=HTTP_404_NOT_FOUND)

            user_credit, quantity = int(user_credit), int(request.data['quantity'])
            if user_credit < quantity or quantity <= 0:
                return Response(dict(message='Deny'), status=HTTP_400_BAD_REQUEST)
            return Response(dict(message='Accept'), status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
