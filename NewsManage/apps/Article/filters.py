# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '自定义文章过滤函数'

import django_filters
from .models import *


# 列表过滤class设置，用,分割数据，实现过滤字段内包含多个要过滤的内容
class ProductFilterSet(django_filters.CharFilter):
    def filter(self, qs, value):
        value = list(filter(None, value.split(",")))
        return super(ProductFilterSet, self).filter(qs=qs, value=value)


# 自定义文章基本信息过滤条件
class ArticleInfoFilter(django_filters.rest_framework.FilterSet):
    # 文章基本信息过滤，支持多个 info_slug
    user_center_article_info = ProductFilterSet(
        field_name='info_slug',
        lookup_expr='in',
        help_text="文章基本信息过滤，支持多个 info_slug"
    )
    # 文章大类过滤
    category = django_filters.CharFilter(
        field_name="category__name",
        help_text="文章一级大类名称"
    )
    # 文章栏目过滤
    item = django_filters.CharFilter(
        field_name="item__name",
        help_text="文章二级栏目名称"
    )
    # 文章标签过滤
    tag = django_filters.CharFilter(
        field_name="tags__name",
        help_text="文章标签名称"
    )

    class Meta:
        model = ArticleInfo
        fields = ["user_center_article_info", "category", "item", "tag"]


# 自定义二级栏目文章信息过滤条件
class ArticleInfoItemFilter(django_filters.rest_framework.FilterSet):
    # 文章标签过滤
    item = django_filters.CharFilter(
        field_name="item",
        help_text="文章二级栏目过滤"
    )

    class Meta:
        model = ArticleInfoItem
        fields = ["item"]
