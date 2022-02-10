from django.urls import path
from .views import OrderApi, OrdersList

urlpatterns = [
    path('orders', OrdersList.as_view()),
    path('order', OrderApi.as_view())
]

