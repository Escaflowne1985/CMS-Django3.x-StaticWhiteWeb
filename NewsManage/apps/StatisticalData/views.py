# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'Statistical 应用的 views 视图配置'

from rest_framework import viewsets
from .serializers import *
from apps.StatisticalData.models import *


# 网站总访问量
class VisitTotalNumberListViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回网站总访问量 total_count</font>\n
    """
    queryset = VisitTotalNumber.objects.filter(id=1)
    serializer_class = VisitTotalNumberSerializer


# 访问IP和模块视图
class VisitIpPartListViewSet(viewsets.CreateModelViewSet):
    """
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** IP访问网站数据</font>\n
    <font size="3" color="blue">1.获取IP信息：xxx.xxx.xxx.xxx</font>\n
    <font size="3" color="blue">2.获取visit_part信息：访问网站模块</font>\n
    <font size="3" color="blue">3.获取visit_time信息：系统当前时间自动创建</font>\n
    """
    queryset = VisitIpPart.objects.all()
    search_fields = ("visit_ip", "visit_part", "visit_time")
    serializer_class = VisitIpPartSerializer


# 每日访问次数视图
class VisitEveryDayNumberListViewSet(viewsets.ReadModelViewSet):
    """
    read:
    <font size="4" color="blue">接口说明：返回网站指定日期的访问数量 visit_count</font>\n
    <font size="3" color="blue">日期数据格式：yyyy-mm-dd</font>\n
    """
    queryset = VisitEveryDayNumber.objects.all()
    serializer_class = VisitEveryDayNumberSerializer
    lookup_field = "date"
