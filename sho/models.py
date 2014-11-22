# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class User(models.Model):
    """
    用户类，姓名、密码、创建时间
    """
    name = models.CharField(verbose_name=u'姓名', max_length=80)
    password = models.CharField(verbose_name=u'密码', max_length=20)
    last_login_time = models.DateTimeField(verbose_name=u'最后登录时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name


class Seller(models.Model):
    """
    卖家类，名称、电话、地址、创建时间
    """
    name = models.CharField(verbose_name=u'名称', max_length=80)
    telephone = models.CharField(verbose_name=u'电话', max_length=80)
    address = models.CharField(verbose_name=u'地址', max_length=200)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name


class Food(models.Model):
    """
    食品类，名称、描述、所属卖家，创建时间
    """
    name = models.CharField(verbose_name=u'名称', max_length=200)
    description = models.TextField(verbose_name=u'描述', )
    seller = models.ForeignKey(Seller)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    """
    订单类，名称、所属用户，所定食品，创建时间
    """
    name = models.CharField(verbose_name=u'名称', max_length=40)
    user = models.OneToOneField(User)
    food = models.OneToOneField(Food)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)