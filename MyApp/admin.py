from django.contrib import admin

# Register your models here.
from MyApp.models import *


class BuyerAdmin(admin.ModelAdmin):
    # bname = models.CharField(max_length=20, unique=True)
    # bgender = models.NullBooleanField(default=None)
    # bage = models.IntegerField(default=0)

    def tellBgender(self):
        if self.bgender:
            return '男'
        else:
            return '女'

    list_display = ['bname',tellBgender,'bage']
    search_fields = ['bname']
    list_filter = ['bgender','bage']


class AccountAdmin(admin.ModelAdmin):
    # amoney = models.FloatField(default=100)
    # ano = models.CharField(max_length=10, unique=True)
    # apwd = models.CharField(default='111111')
    # abuyer = models.OneToOneField(Buyer)

    list_display = ['ano','apwd','abuyer']
    search_fields = ['ano']
    list_filter = ['amoney']


class GoodsAdmin(admin.ModelAdmin):
    # gname = models.CharField(max_length=20, unique=True)
    # gtype = models.CharField(max_length=10)
    # gprice = models.FloatField(default=0)
    # ginfo = models.TextField()
    # gbuyers = models.ManyToManyField(Buyer)

    list_display = ['gname','gtype','gprice','ginfo']
    search_fields = ['gname','gprice','gbuyers']
    list_filter = ['gprice','gtype']

class MySite(admin.AdminSite):
    site_header = '美剁购物系统'
    site_title = '美剁'
mysite = MySite()

mysite.register(Buyer,BuyerAdmin)
mysite.register(Account,AccountAdmin)
mysite.register(Goods,GoodsAdmin)
