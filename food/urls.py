from . import signals

from django.urls import path
from .views import *
from .services import admin_replenish_stock
urlpatterns = [
    path('',index,name="index"),
    path('home_page/',home_page,name="home_page"),
    path('order_page/',order_page,name="order_page"),
    path('order/',main_order,name="main_order"),
    path('admin/replenish_stock/<int:product_id>/<int:amount>', admin_replenish_stock, name='admin_replenish_stock'),

]