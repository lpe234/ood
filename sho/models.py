# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=80)
    password = models.CharField(verbose_name=u'密码', max_length=20)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=80)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    address = models.CharField(verbose_name=u'地址', max_length=200)
    telephone = models.CharField(verbose_name=u'电话', max_length=80)

    def __unicode__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=200)
    description = models.TextField(verbose_name=u'描述', )
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    seller = models.ForeignKey(Seller)

    def __unicode__(self):
        return self.name