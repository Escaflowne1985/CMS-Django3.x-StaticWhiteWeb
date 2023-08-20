# coding:utf-8
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from NewsWeb3.settings import *  # 配置文件Media文件路径
from apps.Article.views import *
from apps.User.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomePage, name='HomePage'),  # 资源主页

    path("captcha/", include('captcha.urls')),  # 验证码url
    # include 各个应用模块
    path('', include("Article.urls")),  # apps.users里面的内容

    # apps.users
    path('UserLogin/', UserLoginView.as_view(), name="UserLogin"),  # 用户登陆
    path('UserLogout/', UserLogoutView.as_view(), name="UserLogout"),  # 用户登出
    path('UserTokenInfo/', UserTokenInfoView.as_view(), name="UserTokenInfo"),  # 用户登陆Token获取
    path("UserRegister/", UserRegisterView.as_view(), name="UserRegister"),  # 用户注册
    path("UserForgotPassword/", UserForgotPasswordView.as_view(), name="UserForgotPassword"),  # 用户忘记密码
    path("UserResetPassWord/<str:OperationType>/<str:Code>/<str:Email>",
         UserResetPasswordView.as_view(), name="UserResetPassWord"),  # 用户重置密码
    path("UserInformationVerification/",
         UserInformationVerificationView.as_view(), name="UserInformationVerification"),  # 用户激活验证
    path("UserArticleFav/<str:info_slug>/", UserArticleFavView.as_view(), name="UserArticleFav"),  # 用户收藏行为js调用
    path("UserArticleRead/", UserArticleReadView.as_view(), name="UserArticleRead"),  # 用户文章列表
    path("UserBuyArticle/<str:info_slug>/", UserBuyArticleView.as_view(), name="UserBuyArticle"),  # 用户购买行为js调用
    # admin 后台部分
    path("AdminUserCenter/", AdminUserCenterView.as_view(), name="AdminUserCenter"),
    path("AdminUserArticleData/", AdminUserArticleDataView.as_view(), name="AdminUserArticleData"),
]
