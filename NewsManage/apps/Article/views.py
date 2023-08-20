# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'Article 应用的 views 视图配置'

from .serializes import *
from rest_framework.pagination import PageNumberPagination
from .filters import *
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers as core_serializers
from apps.User.views import *
from rest_framework import filters
import json


# 后台编辑二级联动视图视图
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class SelectCategoryItemView(LoginRequiredMixin, View):
    def get(self, request):
        # 通过get得到父级选择项
        category_id = request.GET.get('module', '')
        # 筛选出符合父级要求的所有子级，因为输出的是一个集合，需要将数据序列化 serializers.serialize（）
        item = core_serializers.serialize("json", ArticleItem.objects.filter(category_id=int(category_id)))
        # 判断是否存在，输出
        if item:
            return JsonResponse({'item': item})


# API数据显示分页设置
class DataPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = 'page_size'
    PageNumberPagination.page_query_description = '页码数'
    PageNumberPagination.page_size_query_description = '单页显示最大数量 10 条数据'
    max_page_size = 10


# 文章一级大类
class ArticleCategoryViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回审核通过的文章全部一级大类名称列表</font>
    """
    queryset = ArticleCategory.objects.filter(status=1)
    serializer_class = ArticleCategorySerializer
    lookup_field = "name"


# 文章二级栏目
class ArticleItemViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回审核通过的文章全部二级栏目名称列表</font>
    """
    queryset = ArticleItem.objects.filter(status=1)
    serializer_class = ArticleItemSerializer
    lookup_field = "name"


# 文章中文标签
class ArticleTagViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回文章标签的名称列表</font>
    """
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
    lookup_field = "name"


# 文章基本信息
class ArticleInfoListViewSet(viewsets.ListReadModelViewSet):
    """
    read:
    <font size="4" color="blue">接口说明：返回查询的 **info_slug** 的文章基本信息</font>\n
    <font size="3" color="blue">过滤条件包括：</font>\n
    <font size="3" color="blue">1.文章基本信息过滤，支持多个 **info_slug** 使用,分割，**user_center_article_info**</font>\n
    <font size="3" color="blue">2.文章一级大类名称，**category**</font>\n
    <font size="3" color="blue">3.文章二级栏目名称，**item**</font>\n
    <font size="3" color="blue">4.文章标签名称，**tag**</font>\n
    """
    queryset = ArticleInfo.objects.filter(status=1)
    serializer_class = ArticleInfoSerializer
    pagination_class = DataPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filters.SearchFilter.search_description = '检索内容覆盖标题和简介中的内容'
    search_fields = ["title", "summary"]
    filter_class = ArticleInfoFilter
    lookup_field = "info_slug"


# 文章详情
class ArticleDetailListViewSet(viewsets.ReadModelViewSet):
    # permission_classes = (IsAuthenticated, MyPermission)  # 设置用户认证
    # authentication_classes = (JSONWebTokenAuthentication,)  # 只接受 jwt token认证

    """
    list:
    <font size="4" color="blue">接口说明：返回全部已经审核通过的文章列表</font>
    read:
    <font size="4" color="blue">接口说明：返回查询的 **info_slug** 的文章基本信息</font>\n
    <font size="3" color="blue">访问文章详情阅读量 read_num + 1</font>\n
    """
    queryset = ArticleDetail.objects.all()
    serializer_class = ArticleDetailSerializer
    pagination_class = DataPagination
    lookup_field = "detail_slug"

    # 重写retrieve方法（访问内容detail_slug阅读数自动+1）
    def retrieve(self, request, *args, **kwargs):
        try:
            # 阅读详情通过slug信息直接在Info中添加阅读数量
            slug = str(self.request.__dict__["_request"]).split("/")[3]
            info_instance = ArticleInfo.objects.filter(info_slug=str(slug))[0]
            info_instance.read_num += 1
            info_instance.save()
            # 将info中的阅读数复制到InfoHome中
            info_read_num = ArticleInfo.objects.get(info_slug=str(slug)).read_num
            channel_info = ArticleInfoItem.objects.filter(info_slug=str(slug))[0]
            json.loads(channel_info)["read_num"] = info_read_num
            channel_info.save()
            home_info = ArticleInfoHome.objects.filter(info_slug=str(slug))[0]
            json.loads(home_info)["read_num"] = info_read_num
            home_info.save()
            # 构建serializer返回的数据实例
            detail_instance = self.get_object()
            serializer = self.get_serializer(detail_instance)
            return Response(serializer.data)
        except:
            # 构建serializer返回的数据实例
            detail_instance = self.get_object()
            serializer = self.get_serializer(detail_instance)
            return Response(serializer.data)


# 文章附件
class ArticleStorageLinkViewSet(viewsets.ReadModelViewSet):
    """
    read:
    <font size="4" color="blue">接口说明：返回查询的 **info_slug** 的文章附件信息</font>
    """
    queryset = ArticleStorage.objects.all()
    serializer_class = ArticleStorageLinkSerializer
    pagination_class = DataPagination
    lookup_field = "storage_slug"


# 主页文章列表
class ArticleInfoHomeListViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回主页显示文章基本信息列表</font>
    """
    queryset = ArticleInfoHome.objects.all()
    serializer_class = ArticleInfoHomeSerializer


# 栏目文章列表
class ArticleInfoItemListViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回主页显示二级栏目基本信息列表</font>
    """
    queryset = ArticleInfoItem.objects.all()
    pagination_class = DataPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = ArticleInfoItemFilter
    serializer_class = ArticleInfoItemSerializer


# 轮播图
class MyBannerListViewSet(viewsets.ListModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回主banner轮播图内容列表</font>
    """
    queryset = Banner.objects.all()
    serializer_class = MyBannerListSerializer
