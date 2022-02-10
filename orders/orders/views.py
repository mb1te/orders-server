from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OrderSerializer
from .models import Order


def serialize_orders(orders, many):
    serializer = OrderSerializer(orders, many=many)
    return Response(serializer.data)
    return Response(serializer.data)


class OrdersList(APIView):
    """
    View for getting all orders
    """

    def get(self, request):
        orders = Order.objects.all()
        return serialize_orders(orders, many=True)


class OrderApi(APIView):
    """
    View for getting one object or adding objects to db
    """

    def get(self, request):
        try:
            order_id = request.GET.get('order_id', None)
            order = Order.objects.get(id=order_id)
            return serialize_orders(order, many=False)

        except ObjectDoesNotExist:
            return Response(status=400)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 1})
        return Response({'status': 0})
