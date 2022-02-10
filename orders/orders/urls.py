from django.urls import path
from django.views.generic import TemplateView
from .views import OrderApi, OrdersList

urlpatterns = [
    path('', TemplateView.as_view(template_name='docs.html')),
    path('order', OrderApi.as_view()),
    path('orders', OrdersList.as_view()),
]

