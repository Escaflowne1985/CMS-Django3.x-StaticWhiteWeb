# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'StatisticalData 应用部分路由设置'

from rest_framework.routers import DefaultRouter
from .views import *

# 自动生成路由方法
router = DefaultRouter()
# apps.general_data 下的全部路由方法
router.register('VisitTotalNumber', VisitTotalNumberListViewSet, "VisitTotalNumber")  # 网站总访问
router.register('VisitEveryDayNumber', VisitEveryDayNumberListViewSet, "VisitEveryDayNumber")  # 每日访问次数
router.register('VisitIpPart', VisitIpPartListViewSet, "VisitIpPart")  # 访问IP和模块

urlpatterns = [
]
urlpatterns += router.urls
