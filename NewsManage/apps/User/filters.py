# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'API接口数据可搜索过滤定义' \
              '格式为 http://ip:端口号/?搜索的字段名=搜索的字段内容'

import django_filters
from .models import *


# 自定义用户验证
class UserProfileFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(
        field_name="username",
        help_text="过滤的用户名"
    )
    email = django_filters.CharFilter(
        field_name="email",
        help_text="过滤的用户邮箱"
    )
    mobile = django_filters.CharFilter(
        field_name="mobile",
        help_text="过滤的用户手机"
    )

    class Meta:
        model = UserProfile
        fields = ["username", "email", "mobile"]


# 邮箱验证
class UserEmailVerifyRecordFilter(django_filters.rest_framework.FilterSet):
    # 邮箱过滤
    email = django_filters.CharFilter(
        field_name="email",
        help_text="需要被验证的email"
    )
    code = django_filters.CharFilter(
        field_name="code",
        help_text="需要被验证的code"
    )
    send_type = django_filters.CharFilter(
        field_name="send_type",
        help_text="需要被验证的send_type"
    )

    class Meta:
        model = UserEmailVerifyRecord
        fields = ["email", "code", "send_type"]


# 用户阅读、收藏、转发记录查询过滤
class UserFavInfoSlugFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(
        field_name="user__username",
        help_text="通过username查找"
    )
    info_slug = django_filters.CharFilter(
        field_name="info_slug",
        help_text="通过info_slug查找"
    )

    class Meta:
        model = UserFav
        fields = ["username", "info_slug"]


class UserReadInfoSlugFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(
        field_name="user__username",
        help_text="通过username查找"
    )

    class Meta:
        model = UserRead
        fields = ["username"]


class UserShareInfoSlugFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(
        field_name="user__username",
        help_text="通过username查找"
    )

    class Meta:
        model = UserShare
        fields = ["username"]


# 用户订单信息过滤
class UserOrderFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(
        field_name="user__username",
        help_text="通过username查找"
    )

    class Meta:
        model = UserOrder
        fields = ["username"]
