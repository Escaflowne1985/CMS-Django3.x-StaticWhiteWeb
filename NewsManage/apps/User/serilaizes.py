# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'User 应用 serializes API 序列化配置'

from apps.User.models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# 用户列表
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["is_superuser", "first_name", "last_name", "is_staff", "groups", "user_permissions"]


# 用户注册
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "password", "mobile", "email", "nick_name", "is_active"]


# 用户信息更新
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["is_superuser", "first_name", "last_name", "is_staff", "groups", "user_permissions", "date_joined",
                   "last_login"]


# 用户订阅序列化
class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ["email"]


# 用户邮件序列化
class UserEmailVerifyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmailVerifyRecord
        fields = ["code", "email", "send_type", "send_time"]


# 用户收藏序列化
class UserFavSerializer(serializers.ModelSerializer):
    # 在Serializer中简化用户数据列表，直接显示用户名称
    username = serializers.CharField(source='user.username')

    class Meta:
        model = UserFav
        fields = ['id', 'username', 'info_slug']

    def create(self, validated_data):
        # print("validated_data:", validated_data)
        user_id = UserProfile.objects.get(username=validated_data['user']["username"])
        # user_fav表中的新增记录，这里由于是使用的外键关联需要查询后写入
        user_fav_data = UserFav.objects.create(
            user_id=user_id.id,
            info_slug=validated_data['info_slug'],
            add_time=timezone.now()
        )
        return user_fav_data


# 用户浏览序列化
class UserReadSerializer(serializers.ModelSerializer):
    # 在Serializer中简化用户数据列表，直接显示用户名称
    username = serializers.CharField(source='user.username')

    def create(self, validated_data):
        print("validated_data:", validated_data)
        user_id = UserProfile.objects.get(username=validated_data['user']["username"])
        # user_read表中的新增记录，这里由于是使用的外键关联需要查询后写入
        user_read_data = UserRead.objects.create(
            user_id=user_id.id,
            info_slug=validated_data['info_slug'],
            add_time=timezone.now()
        )
        return user_read_data

    class Meta:
        model = UserRead
        fields = ['username', 'info_slug']


# 用户分享序列化
class UserShareSerializer(serializers.ModelSerializer):
    # 在Serializer中简化用户数据列表，直接显示用户名称
    username = serializers.CharField(source='user.username')

    def create(self, validated_data):
        # print("validated_data:", validated_data)
        user_id = UserProfile.objects.get(username=validated_data['user']["username"])
        # user_share表中的新增记录，这里由于是使用的外键关联需要查询后写入
        user_share_data = UserShare.objects.create(
            user_id=user_id.id,
            info_slug=validated_data['info_slug'],
            share_type=validated_data['share_type'],
            add_time=timezone.now()
        )
        return user_share_data

    class Meta:
        model = UserShare
        fields = ['username', 'info_slug', 'share_type']


# 用户订单序列化
class UserOrderSerializer(serializers.ModelSerializer):
    # 在Serializer中简化用户数据列表，直接显示用户名称
    username = serializers.CharField(source='user.username')

    def create(self, validated_data):
        # print("validated_data:", validated_data)
        user_id = UserProfile.objects.get(username=validated_data['user']["username"])
        # user_order表中的新增记录，这里由于是使用的外键关联需要查询后写入
        user_order_data = UserOrder.objects.create(
            user_id=user_id.id,
            info_slug=validated_data['info_slug'],
            consumption_integral=validated_data['consumption_integral'],
            add_time=timezone.now()
        )
        return user_order_data

    class Meta:
        model = UserOrder
        fields = ['username', 'info_slug', 'consumption_integral']


# 用户操作日志序列化
class UserServerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerLog
        fields = ["user", "time", "type", "content", "status", "remark"]
