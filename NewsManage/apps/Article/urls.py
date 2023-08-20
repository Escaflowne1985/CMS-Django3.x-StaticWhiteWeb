# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'Article 应用部分路由设置'

from rest_framework.routers import DefaultRouter
from apps.Article.views import *
from django.conf.urls import url

router = DefaultRouter()
# apps.Article 下的全部路由方法
router.register('ArticleCategory', ArticleCategoryViewSet, 'ArticleCategory')  # 文章一级大类
router.register('ArticleItem', ArticleItemViewSet, 'ArticleItem')  # 文章二级栏目
router.register('ArticleTag', ArticleTagViewSet, 'ArticleTag')  # 文章标签
router.register('ArticleInfo', ArticleInfoListViewSet, "ArticleInfo")  # 文章基本信息
router.register('ArticleDetail', ArticleDetailListViewSet, "ArticleDetail")  # 文章详情
router.register('ArticleStorageLink', ArticleStorageLinkViewSet, "ArticleStorageLink")  # 文章附件
router.register('ArticleInfoHomeList', ArticleInfoHomeListViewSet, "ArticleInfoHomeList")  # 主页文章
router.register('ArticleInfoItemList', ArticleInfoItemListViewSet, "ArticleInfoItemList")  # 栏目文章
router.register('MyBannerList', MyBannerListViewSet, "MyBannerList")  # 图片轮播

urlpatterns = [
    # 后台编辑二级联动视图 url
    url(r'SelectCategoryItemView', SelectCategoryItemView.as_view(), name='SelectCategoryItemView'),
]
urlpatterns += router.urls
