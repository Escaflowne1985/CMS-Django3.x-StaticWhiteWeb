"""NewsManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

# 建立一个路由对象
router = DefaultRouter()
# 将我们的路由注册到url里
from django.conf.urls import url
from django.views import static
from django.conf import settings
from apps.Article.views import *

# from general_data.views import *

urlpatterns = [
    # 后台管理程序
    path('xadmin/', xadmin.site.urls),
    # API接口 Debug
    path('ApiDebug/', get_swagger_view(title='内容管理API调试')),
    # API接口 文档
    path('ApiDocs/', include_docs_urls(title="内容管理API文档")),

    # include 各个应用模块
    path('UserSettings/', include("User.urls")),  # apps.users里面的内容
    path('ArticleSettings/', include("Article.urls")),  # apps.articles里面的内容
    path('StatisticalDataSettings/', include("StatisticalData.urls")),  # apps.general_data里面的内容

    # 静态文件和多媒体文件路由
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    # Django富文本编辑器路由
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 二级下来菜单联动
    url(r'SelectCategoryItem/', SelectCategoryItemView.as_view(), name='SelectCategoryItem'),
]
urlpatterns += router.urls
# Debug =True
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
