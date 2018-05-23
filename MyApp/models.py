from django.db import models


# Create your models here.
class Buyer(models.Model):
    bname = models.CharField(max_length=20, unique=True)
    bgender = models.NullBooleanField(default=None)
    bage = models.IntegerField(default=0)

    def __str__(self):
        return self.bname


class Account(models.Model):
    amoney = models.FloatField(default=100)
    ano = models.CharField(max_length=10, unique=True)
    apwd = models.CharField(max_length=6,default='111111')
    abuyer = models.OneToOneField(Buyer)

    def __str__(self):
        return self.ano


class Order(models.Model):
    # ono = models.AutoField(primary_key=True,default=1)
    odatetime = models.DateTimeField(auto_now_add=True)
    omoney = models.FloatField(default=0)
    omsg = models.CharField(max_length=200,null=True)
    obuyer = models.ForeignKey(Buyer)

    def __str__(self):
        return "Order{obuyer="+self.obuyer.bname+",omoney="+str(self.omoney)+"}"


class Goods(models.Model):
    gname = models.CharField(max_length=20, unique=True)
    gtype = models.CharField(max_length=10)
    gprice = models.FloatField(default=0)
    ginfo = models.TextField()
    gbuyers = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.gname
