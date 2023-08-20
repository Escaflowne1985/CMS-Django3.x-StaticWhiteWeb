# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '后端API users的models' \
              '1.用户列表模型' \
              '2.用户订阅模型' \
              '3.用户邮件模型' \
              '4.用户收藏模型' \
              '5.用户浏览模型' \
              '6.用户分享模型' \
              '7.用户订单模型' \
              '8.用户日志模型'

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from apps.Configuration.config_choose import *


# 用户列表模型
class UserProfile(AbstractUser):
    actual_name = models.CharField(
        max_length=10, verbose_name="用户姓名",
        help_text="真实姓名",
        null=True, blank=True, unique=False
    )
    nick_name = models.CharField(
        max_length=20, verbose_name="用户昵称",
        help_text="昵称",
        null=True, blank=True, unique=False
    )
    gender = models.CharField(
        max_length=9, verbose_name="用户性别",
        help_text="性别",
        choices=GENDER_CHOICES, default="未定义"
    )
    birthday = models.DateField(
        verbose_name="用户生日",
        help_text="生日",
        null=True, blank=True
    )
    address = models.CharField(
        max_length=100, verbose_name="联系地址",
        help_text="地址信息",
        default="", blank=True
    )
    mobile = models.CharField(
        max_length=11, verbose_name="联系电话",
        help_text="移动电话",
        null=True, blank=True
    )
    user_image = models.ImageField(
        upload_to="UserImage", default="UserImage/default.png",
        verbose_name="用户头像", help_text="头像图片",
        null=True, blank=True
    )
    user_role = models.CharField(
        max_length=20,
        verbose_name="用户角色", help_text="角色",
        choices=ROLE_CHOICES, default="游客"
    )
    integral = models.IntegerField(
        default=0,
        verbose_name="用户积分", help_text="积分",
    )
    vip_level = models.IntegerField(
        default=0,
        verbose_name="用户等级", help_text="等级",
    )
    vip_exp = models.IntegerField(
        default=0,
        verbose_name="用户经验", help_text="经验值",
    )

    class Meta:
        verbose_name = "用户信息列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 用户订阅模型
class UserSubscription(models.Model):
    email = models.CharField(
        max_length=100, verbose_name="用户邮箱",
        unique=False
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='创建时间', help_text='默认创建时系统时间'
    )

    class Meta:
        verbose_name = "用户订阅列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


# 用户邮件模型
class UserEmailVerifyRecord(models.Model):
    code = models.CharField(
        max_length=20,
        verbose_name="验证码", help_text="系统随机生成的邮件验证码"
    )
    email = models.EmailField(
        max_length=100,
        verbose_name="接收邮件邮箱", help_text="用户使用邮件功能接受内容的注册时的邮箱"
    )
    SEND_CHOICES = (
        ("register", "注册"),
        ("forgot", "找回密码"),
        ("update_email", "修改密码")
    )
    send_type = models.CharField(
        choices=SEND_CHOICES, max_length=20,
        verbose_name="验证码类型", help_text="用户使用邮件功能的类型"
    )
    send_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="邮件发送时间", help_text='默认创建时系统时间'
    )

    class Meta:
        verbose_name = "邮箱功能列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


# 用户收藏模型
class UserFav(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name='user_fav', on_delete=models.CASCADE,
        verbose_name="用户id", help_text="必须为Admin系统中的用户"
    )
    info_slug = models.CharField(
        max_length=100, default="",
        verbose_name="收藏文章slug", help_text="文章的slug信息"
    )
    add_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="收藏时间", help_text='默认创建时系统时间'
    )

    class Meta:
        verbose_name = '用户收藏信息'
        verbose_name_plural = verbose_name
        unique_together = ("user", "info_slug")

    def __str__(self):
        return self.user.username


# 用户浏览模型
class UserRead(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name='user_read', on_delete=models.CASCADE,
        verbose_name="用户id", help_text="必须为Admin系统中的用户"
    )
    info_slug = models.CharField(
        max_length=100, default="",
        verbose_name="浏览文章slug", help_text="文章的slug信息"
    )
    add_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="浏览时间", help_text='默认创建时系统时间'
    )

    class Meta:
        verbose_name = '用户浏览信息'
        verbose_name_plural = verbose_name
        unique_together = ("user", "info_slug", "add_time")

    def __str__(self):
        return self.user.username


# 用户分享模型
class UserShare(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name='user_share', on_delete=models.CASCADE,
        verbose_name="用户id", help_text="必须为Admin系统中的用户"
    )
    info_slug = models.CharField(
        max_length=100, default="",
        verbose_name="分享文章slug", help_text="文章的slug信息"
    )
    add_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="分享时间", help_text='默认创建时系统时间'
    )
    share_type = models.CharField(
        max_length=30, default="",
        verbose_name='分享方式', help_text="用户使用的分享文章的方式"
    )

    class Meta:
        verbose_name = '用户分享信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


# 用户订单模型
class UserOrder(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name='user_order', on_delete=models.CASCADE,
        verbose_name="用户id", help_text="必须为Admin系统中的用户"
    )
    info_slug = models.CharField(
        max_length=100, default="",
        verbose_name="购买文章slug", help_text="文章的slug信息"
    )
    add_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="购买时间", help_text='默认创建时系统时间'
    )
    consumption_integral = models.IntegerField(
        default=0,
        verbose_name="使用积分", help_text='购买文章附件使用的积分'
    )

    class Meta:
        verbose_name = '用户订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


# 用户日志模型
class UserServerLog(models.Model):
    user = models.CharField(
        max_length=100, default="",
        verbose_name="操作用户", help_text="记录的用户信息"
    )
    time = models.DateTimeField(
        default=timezone.now,
        verbose_name="操作时间", help_text='默认创建时系统时间'
    )
    type = models.CharField(
        max_length=100, default="",
        verbose_name="操作类型", help_text="记录的操作信息类型"
    )
    content = models.TextField(
        default="",
        verbose_name="日志内容", help_text="记录的操作日志内容",
        null=True, blank=True
    )
    StatusChoices = (
        ("0", "失败"),
        ("1", "成功")
    )
    status = models.CharField(
        choices=StatusChoices, max_length=1, default=0,
        verbose_name='操作状态', help_text="记录的操作状态"
    )
    remark = models.TextField(
        default="",
        verbose_name="日志备注", help_text="记录的日志备注",
        null=True, blank=True
    )

    class Meta:
        verbose_name = '用户行为日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
