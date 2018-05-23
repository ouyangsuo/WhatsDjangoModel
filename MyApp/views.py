import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from MyApp.models import *


def addBuyer(request):
    b = Buyer()
    b.bname = 'Buyer-'+str(int(time.time()))
    b.save()
    return HttpResponse('用户添加成功'+b.bname)


def deleteBuyer(request):
    b = Buyer.objects.last()
    b.delete()
    return HttpResponse('用户删除成功'+b.bname)


def updateBuyer(request):
    b = Buyer.objects.last()
    b.bname = 'new'+b.bname
    b.save()
    return HttpResponse('用户修改成功'+b.bname)


def queryBuyer(request):
    bs = Buyer.objects.all()
    ret = ''
    for b in bs:
        ret+=b.bname+";"
    return HttpResponse('用户查询成功'+ret)


def getAccount(request,bid):
    b = Buyer.objects.get(pk=bid)
    account = b.account
    return HttpResponse(account.ano)


def buy(request,bid,gid):
    b = Buyer.objects.get(pk=bid)
    g = Goods.objects.get(pk=gid)
    g.gbuyers.add(b)
    g.save()

    o = Order()
    o.obuyer = b
    o.omoney = g.gprice
    o.omsg = g.gname
    o.save()
    return HttpResponse(o)


def getOrders(request,bid):
    b = Buyer.objects.get(pk=bid)
    bos = b.order_set.all()
    ret = ''
    for o in bos:
        ret += str(o.id)+";"
    return HttpResponse(ret)


def getBuyerGoods(request,bid):
    b = Buyer.objects.get(pk=bid)
    gs = b.goods_set
    ret = ''
    for g in gs:
        ret += g.gname+";"
    return HttpResponse(ret)


def getGoodsBuyers(request,gid):
    g = Goods.objects.get(pk=gid)
    bs = g.gbuyers.all()
    ret = ''
    for b in bs:
        ret += b.bname+";"
    return HttpResponse(ret)