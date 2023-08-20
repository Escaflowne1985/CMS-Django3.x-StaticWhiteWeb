# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'StatisticalData 应用 serializes API 序列化配置'

from rest_framework import serializers
from apps.StatisticalData.models import *


# 网站总访问序列化
class VisitTotalNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitTotalNumber
        fields = ["total_count"]


# 访问IP和模块序列化
class VisitIpPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitIpPart
        fields = ["visit_ip", "visit_part"]

    def create(self, validated_data):
        # print("validated_data:", validated_data)
        visit_ip = validated_data["visit_ip"]
        visit_part = validated_data["visit_part"]

        # IP访问记录写入
        VisitIpPart.objects.create(
            visit_ip=visit_ip,
            visit_part=visit_part,
            visit_time=timezone.now()
        )

        # 网站总访问次数统计
        count_nums = VisitTotalNumber.objects.filter(id=1)
        if count_nums:
            count_nums = count_nums[0]
            count_nums.total_count += 1
        else:
            count_nums = VisitTotalNumber()
            count_nums.total_count = 1
        count_nums.save()

        # IP访问统计
        ip_exist = VisitEveryIpCount.objects.filter(visit_ip=str(visit_ip))
        if ip_exist:  # 判断是否存在该ip
            uobj = ip_exist[0]
            uobj.visit_count += 1
        else:
            uobj = VisitEveryIpCount()
            uobj.visit_ip = visit_ip
            uobj.visit_count = 1
        uobj.save()

        # 单日访问统计
        date = timezone.now().date()
        today = VisitEveryDayNumber.objects.filter(date=date)
        if today:
            temp = today[0]
            temp.visit_count += 1
        else:
            temp = VisitEveryDayNumber()
            temp.dayTime = date
            temp.visit_count = 1
        temp.save()


# 访问IP的总数序列化
class VisitEveryIpCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitEveryIpCount
        fields = ["visit_ip", "visit_count"]


# 每日访问次数序列化
class VisitEveryDayNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitEveryDayNumber
        fields = ["visit_count"]
