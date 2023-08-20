# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '统计数据的models'

from django.db import models
from django.utils import timezone


# 网站总访问模型
class VisitTotalNumber(models.Model):
    total_count = models.IntegerField(
        default=0,
        verbose_name='网站访问总次数', help_text='统计的网站被访问的总次数'
    )

    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.total_count)


# 每日访问次数模型
class VisitEveryDayNumber(models.Model):
    date = models.DateField(
        default=timezone.now,
        verbose_name='统计日期', help_text='通过后台自动计算的按照日期聚合访问次数'
    )
    visit_count = models.IntegerField(
        default=0,
        verbose_name='统计次数', help_text='当日网站访问总次数'
    )

    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.date)


# 访问IP和模块模型
class VisitIpPart(models.Model):
    visit_ip = models.CharField(
        max_length=30,
        verbose_name='IP地址', help_text='访问网站的IP地址信息记录'
    )
    visit_address = models.CharField(
        max_length=100,
        verbose_name="访问IP地区"
    )
    visit_part = models.CharField(
        max_length=30,
        verbose_name='内容模块', help_text='访问网站的具体内容模块'
    )
    visit_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='访问时间', help_text='默认创建时系统时间'
    )

    class Meta:
        verbose_name = 'IP访问明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.visit_ip)


# 访问IP的总数模型
class VisitEveryIpCount(models.Model):
    visit_ip = models.CharField(
        max_length=30,
        verbose_name='IP地址', help_text='访问网站的IP地址信息记录'
    )
    visit_count = models.IntegerField(
        default=0,
        verbose_name='IP访问次数', help_text='通过后台自动计算的IP聚合访问次数'
    )

    class Meta:
        verbose_name = 'IP访问汇总'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.visit_ip
