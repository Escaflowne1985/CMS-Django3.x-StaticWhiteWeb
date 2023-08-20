# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'User 应用部分路由设置'

from django.urls import include, path
from apps.User.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# 自动生成路由方法
router = DefaultRouter()
# apps.users 下的全部路由方法
router.register('UserProfile', UserProfileViewSet, "UserProfile")  # 用户列表路由
router.register('UserProfileUpdate', UserProfileUpdateViewSet, "UserProfileUpdate")  # 用户信息更新
router.register('UserSubscription', UserSubscriptionViewSet, "UserSubscription")  # 用户订阅
router.register('UserRegister', UserRegisterViewSet, "UserRegister")  # 用户注册路由
router.register('UserEmailVerifyRecord', UserEmailVerifyRecordViewSet, "UserEmailVerifyRecord")  # 用户邮件路由
router.register('UserFav', UserFavViewSet, "UserFav")  # 用户收藏路由
router.register('UserRead', UserReadViewSet, "UserRead")  # 用户浏览路由
router.register('UserShare', UserShareViewSet, "UserShare")  # 用户分享路由
router.register('UserOrder', UserOrderViewSet, "UserOrder")  # 用户订单路由
router.register('UserServerLog', UserServerLogViewSet, "UserServerLog")  # 用户列表用户操作日志路由

urlpatterns = [
    # path('user_token/',CreateUserTokenViewSet.as_view(),name="user_token"),# 用户Token
    path('token_login/', obtain_jwt_token),  # 获取token，登录视图
    path('token_refresh/', refresh_jwt_token),  # 刷新token
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # 认证地址
]
urlpatterns += router.urls  # 模块地址
