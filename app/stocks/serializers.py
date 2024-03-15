from rest_framework import serializers

from stocks.models import BuyingStock


class BuyStockBodySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    stockname = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()


class BuyingStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingStock
        fields = '__all__'
