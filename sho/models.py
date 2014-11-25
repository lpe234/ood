# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class User(models.Model):
    """
    用户类，姓名、密码、创建时间
    """
    username = models.CharField(verbose_name=u'姓名', max_length=80)
    password = models.CharField(verbose_name=u'密码', default='rose123', max_length=20)
    last_login_time = models.DateTimeField(verbose_name=u'最后登录时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class Seller(models.Model):
    """
    卖家类，名称、电话、地址、创建时间
    """
    name = models.CharField(verbose_name=u'名称', max_length=80)
    telephone = models.CharField(verbose_name=u'电话', max_length=80)
    address = models.CharField(verbose_name=u'地址', max_length=200)
    info = models.TextField(verbose_name=u'附加信息', blank=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'卖家'
        verbose_name_plural = u'卖家'


class Food(models.Model):
    """
    食品类，名称、描述、所属卖家，创建时间
    """
    name = models.CharField(verbose_name=u'名称', max_length=200)
    description = models.TextField(verbose_name=u'描述', blank=True)
    seller = models.ForeignKey(Seller)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'食品'
        verbose_name_plural = u'食品'


class Order(models.Model):
    """
    订单类，名称、所属用户，所定食品，创建时间
    """
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    info = models.TextField(verbose_name=u'附加信息', blank=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.user.name

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = u'订单'