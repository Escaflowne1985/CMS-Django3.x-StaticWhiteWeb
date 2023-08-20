# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'User 应用的 views 视图配置'

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.User.serilaizes import *
from apps.User.filters import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from rest_framework.permissions import IsAuthenticated, BasePermission


# JWT 权限设置，用于权限设置是否有权访问
class MyPermission(BasePermission):
    message = '自定义的返回信息'

    def has_permission(self, request, view):  # 列表数据
        # # 这个函数返回True或者False，True表示有权限，False表示没有权限,这个函数同时有三个参数，最后一个是view
        # if request.user.id == 0:
        #     return False
        # else:
        return True

    def has_object_permission(self, request, view, obj):  # 对象数据
        """用户是否有权限访问添加了权限控制类的数据对象"""
        # 需求：用户能够访问id为1，3的对象，其他的不能够访问
        if request.user.is_active == 1:
            return True
        else:
            return False


# 用户基本信息
class UserProfileViewSet(viewsets.ListReadModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：通过字段查询用户数据信息</font>\n
    <font size="3" color="blue">1.用户名：username </font>\n
    <font size="3" color="blue">2.用户邮箱：email </font>\n
    <font size="3" color="blue">3.用户手机：mobile </font>\n
    read:
    <font size="4" color="blue">接口说明：返回查询的 **username** 的用户基本信息</font>
    """
    queryset = UserProfile.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserProfileFilter
    serializer_class = UserProfileSerializer
    lookup_field = "username"


# 用户基本信息修改
class UserProfileUpdateViewSet(viewsets.UpdateMoldelViewSet):
    """
    update:
    <font size="4" color="blue">接口说明：Post更新 **username** 的用户基本信息</font>
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileUpdateSerializer
    lookup_field = "username"


# 用户注册
class UserRegisterViewSet(viewsets.CreateModelViewSet):
    """
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 用户注册信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    <font size="3" color="blue">2.密码：password 必备</font>\n
    <font size="3" color="blue">3.电话：mobile 可选</font>\n
    <font size="3" color="blue">4.用户昵称：nick_name 可选</font>\n
    <font size="3" color="blue">5.激活状态：is_active 可选</font>\n
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserRegisterSerializer


# 用户订阅网站信息
class UserSubscriptionViewSet(viewsets.CreateModelViewSet):
    """
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 用户订阅网站预留Email信息</font>\n
    <font size="3" color="blue">1.邮箱：email 必备</font>\n
    """
    queryset = UserSubscription.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['email']
    serializer_class = UserSubscriptionSerializer


# 用户邮件验证
class UserEmailVerifyRecordViewSet(viewsets.ListCreateModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回用户邮箱、验证码列表支持条件查询</font>\n
    <font size="3" color="blue">1.邮箱：email 必备</font>\n
    <font size="3" color="blue">2.验证码：code 必备</font>\n
    <font size="3" color="blue">3.验证类型：send_type 必备</font>\n
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 用户邮件验证Email信息</font>\n
    <font size="3" color="blue">1.邮箱：email 必备</font>\n
    <font size="3" color="blue">2.验证码：code 必备</font>\n
    <font size="3" color="blue">3.验证类型：send_type 必备</font>\n
    """
    queryset = UserEmailVerifyRecord.objects.all()
    serializer_class = UserEmailVerifyRecordSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserEmailVerifyRecordFilter


# 用户收藏
class UserFavViewSet(viewsets.ListCreateDeleteModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回查询的 **username** 的收藏的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 收藏内容 **info_slug** 的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    <font size="3" color="blue">2.文章slug：info_slug 必备</font>\n
    delete:
    <font size="4" color="blue">接口说明：Post提交 **删除** 收藏内容 **info_slug** 的数据信息</font>\n
    <font size="3" color="blue">通过 username 和 info_slug 查找对应 id 删除</font>\n
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserFavInfoSlugFilter


# 用户浏览视图
class UserReadViewSet(viewsets.ListCreateModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回查询的 **username** 的浏览的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 浏览内容 **info_slug** 的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    <font size="3" color="blue">2.文章slug：info_slug 必备</font>\n
    """
    queryset = UserRead.objects.all()
    serializer_class = UserReadSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserReadInfoSlugFilter


# 用户分享视图
class UserShareViewSet(viewsets.ListCreateModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回查询的 **username** 的分享的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 分享内容 **info_slug** 的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    <font size="3" color="blue">2.文章slug：info_slug 必备</font>\n
    """
    queryset = UserShare.objects.all()
    serializer_class = UserShareSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserShareInfoSlugFilter


# 用户订单视图
class UserOrderViewSet(viewsets.ListCreateModelViewSet):
    """
    list:
    <font size="4" color="blue">接口说明：返回查询的 **username** 的订单的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 订单内容 **info_slug** 的数据信息</font>\n
    <font size="3" color="blue">1.用户名：username 必备</font>\n
    <font size="3" color="blue">2.文章slug：info_slug 必备</font>\n
    <font size="3" color="blue">3.使用积分：consumption_integral 必备</font>\n
    """
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserOrderFilter


# 用户操作日志视图
class UserServerLogViewSet(viewsets.CreateModelViewSet):
    """
    create:
    <font size="4" color="blue">接口说明：Post提交 **新增** 用户系统操作的数据信息</font>
    """
    queryset = UserServerLog.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['user', ]
    serializer_class = UserServerLogSerializer
    lookup_field = "user"

# from rest_framework import permissions
# from rest_framework_simplejwt import authentication
# from rest_framework.response import Response
# from django.forms.models import model_to_dict
# from rest_framework.views import APIView
#
#
# class GetUserViewSet(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = (authentication.JWTAuthentication,)
#
#     def get(self, request, *args, **kwargs):
#         queryset = UserProfile.objects.filter(username=request.user)[0]
#         user = model_to_dict(queryset)
#         return Response(str(user))

# import json
# from django.views.decorators.csrf import csrf_exempt
# # 生成用户Token
# class CreateUserTokenViewSet(View):
#     def post(self, request, *args, **kwargs):
#         username = json.loads(request._body)['username']
#         password = json.loads(request._body)['password']
#         user = auth.authenticate(username=username, password=password)
#         if not user:
#             return JsonResponse({"code": 0,
#                                  "msg": "用户名或密码不对!"})
#         # 删除原有的Token
#         old_token = Token.objects.filter(user=user)
#         old_token.delete()
#         # 创建新的Token
#         token = Token.objects.create(user=user)
#         return JsonResponse({"code": 0,
#                              "msg": "login success!",
#                              "username": user.username,
#                              "token": token.key})
#
#     # 这里要跳过CSRF验证
#     @csrf_exempt
#     def dispatch(self, *args, **kwargs):
#         return super(UserTokenViewSet, self).dispatch(*args, **kwargs)
# # 用户Token视图列表
# class UserTokenViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Token.objects.all()
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # django_filter 的三种方式
#     serializer_class = UserTokenSerializer
#     lookup_field = "user_id"
