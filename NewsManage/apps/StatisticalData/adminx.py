# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = 'StatisticalData 应用 Adminx 后台管理控制配置'

import xadmin
from .models import *


# 网站总访问管理
class VisitTotalNumberAdmin(object):
    list_display = ['total_count']
    show_bookmarks = False
    list_per_page = 30
    readonly_fields = ['total_count']


# 每日访问次数管理
class VisitEveryDayNumberAdmin(object):
    list_display = ['date', 'visit_count']
    show_bookmarks = False
    list_per_page = 30
    readonly_fields = ['date', 'visit_count']


# 访问IP和模块管理
class VisitIpPartAdmin(object):
    list_display = ['visit_ip', 'visit_time', 'visit_address', 'visit_part']
    show_bookmarks = False
    list_per_page = 30
    readonly_fields = ['visit_ip', 'visit_part']


# 访问IP的总数管理
class VisitEveryIpCountAdmin(object):
    list_display = ['visit_ip', 'visit_count']
    show_bookmarks = False
    list_per_page = 30
    readonly_fields = ['visit_ip', 'visit_count']


xadmin.site.register(VisitTotalNumber, VisitTotalNumberAdmin)
xadmin.site.register(VisitEveryDayNumber, VisitEveryDayNumberAdmin)
xadmin.site.register(VisitIpPart, VisitIpPartAdmin)
xadmin.site.register(VisitEveryIpCount, VisitEveryIpCountAdmin)
