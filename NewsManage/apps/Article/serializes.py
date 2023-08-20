# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'Article 应用 serializes API 序列化配置'

from rest_framework import serializers
from .models import *


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ["name"]


class ArticleItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = ArticleItem
        fields = ["category_name", "name"]


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ["name"]


class ArticleInfoSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source='item.name')
    category = serializers.CharField(source='category.name')
    author = serializers.CharField(source='article_author.username')
    tags = ArticleTagSerializer(many=True)

    class Meta:
        model = ArticleInfo
        exclude = ["article_author", "audit_user", "source_url", "province", "city", "ai_type"]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = "__all__"


class ArticleStorageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleStorage
        fields = "__all__"


class ArticleInfoHomeSerializer(serializers.ModelSerializer):
    # article_item = serializers.CharField(source='article_item.item_name')  # 解析获取大类类别内容信息
    # article_author = serializers.CharField(source='article_author.username')  # 解析获取作者名称内容信息
    # article_tags = ArticleTagSerializer(many=True)

    class Meta:
        model = ArticleInfoHome
        fields = "__all__"


class ArticleInfoItemSerializer(serializers.ModelSerializer):
    # article_item = serializers.CharField(source='article_item.item_name')  # 解析获取大类类别内容信息
    # article_author = serializers.CharField(source='article_author.username')  # 解析获取作者名称内容信息
    # article_tags = ArticleTagSerializer(many=True)

    class Meta:
        model = ArticleInfoItem
        fields = "__all__"


# 轮播图序列化
class MyBannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
