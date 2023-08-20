# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = ''

from django.urls import path, re_path
from .views import *

app_name = 'Article'

urlpatterns = [
    path('GetArticleDetail/<str:info_slug>', GetArticleDetail, name='GetArticleDetail'),
    path('GetArticleItemInfo/<str:category>/<str:item>/<int:page>', GetArticleItemInfo, name='GetArticleItemInfo'),
    path('GetArticleSearchInfoPost', GetArticleSearchInfoPost, name='GetArticleSearchInfoPost'),
    path('GetArticleSearchInfoGet/<str:search_data>/<int:page>', GetArticleSearchInfoGet, name='GetArticleSearchInfoGet'),
    # 用户订阅邮件
    path("UserSubscription/", UserSubscription, name="UserSubscription"),
]
