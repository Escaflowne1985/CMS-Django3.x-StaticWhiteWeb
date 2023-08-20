# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = 'User 应用 Adminx 后台管理控制配置'

from django.contrib.auth import get_user_model
import xadmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *
from xadmin.layout import *

# 获取全局user管理
User = get_user_model()


# 自定义用户创建表单(创建用户应用密码保存为加密方式)
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "user_role")
        field_classes = {"username": UsernameField, }


# 用户信息管理
class UserProfileAdmin(object):
    list_display = ['username', 'user_role', 'nick_name', 'integral', 'email']
    readonly_fields = ['date_joined', 'last_login']
    show_bookmarks = False

    # 配置自定义用户创建表MyUserCreationForm
    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = MyUserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserProfileAdmin, self).get_model_form(**kwargs)

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('用户信息',
                             'username', 'actual_name', 'nick_name', 'gender',
                             'address', 'mobile', 'email', 'birthday',
                             ),
                    Fieldset(('用户数据'),
                             Row('integral', 'vip_level', 'vip_exp'),
                             Row('last_login', 'date_joined'),
                             ),
                    Fieldset(None,
                             'password', 'user_permissions', 'first_name', 'last_name',
                             **{"style": "display:None"}),
                ),
                Side(
                    Fieldset(('用户'),
                             'user_image',
                             ),
                    Fieldset(('用户权限'),
                             'groups',
                             ),
                    Fieldset(('用户身份'),
                             'user_role', 'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserProfileAdmin, self).get_form_layout()


# 用户订阅管理
class UserSubscriptionAdmin(object):
    list_display = ['email', 'created_date']
    show_bookmarks = False


# 用户邮件管理
class UserEmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    show_bookmarks = False


# 用户收藏管理
class UserFavAdmin(object):
    list_display = ['user', 'info_slug', 'add_time']
    show_bookmarks = False


# 用户浏览管理
class UserReadAdmin(object):
    list_display = ['user', 'info_slug', 'add_time']
    show_bookmarks = False


# 用户分享管理
class UserShareAdmin(object):
    list_display = ['user', 'share_type', 'info_slug', 'add_time']
    show_bookmarks = False


# 用户订单管理
class UserOrderAdmin(object):
    list_display = ['user', 'consumption_integral', 'info_slug', 'add_time']
    show_bookmarks = False


# 用户日志管理
class UserServerLogAdmin(object):
    list_display = ['user', 'time', 'type', 'status', 'content']
    show_bookmarks = False


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(UserSubscription, UserSubscriptionAdmin)
xadmin.site.register(UserEmailVerifyRecord, UserEmailVerifyRecordAdmin)
xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserRead, UserReadAdmin)
xadmin.site.register(UserShare, UserShareAdmin)
xadmin.site.register(UserOrder, UserOrderAdmin)
xadmin.site.register(UserServerLog, UserServerLogAdmin)
