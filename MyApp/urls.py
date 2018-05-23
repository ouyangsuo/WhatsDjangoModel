from django.conf.urls import url, include
from django.contrib import admin

from MyApp import views
from MyApp.admin import mysite

urlpatterns = [
    url(r'^addbuyer/', views.addBuyer),
    url(r'^deletebuyer/', views.deleteBuyer),
    url(r'^updatebuyer/', views.updateBuyer),
    url(r'^querybuyer/', views.queryBuyer),

    url(r'^getaccount/(\d+)/', views.getAccount),
    url(r'^buy/(\d+)/(\d+)/', views.buy),
    url(r'^getorders/(\d+)/', views.getOrders),
    url(r'^getbuyergoods/(\d+)/', views.getBuyerGoods),
    url(r'^getgoodsbuyers/(\d+)/', views.getGoodsBuyers),
]