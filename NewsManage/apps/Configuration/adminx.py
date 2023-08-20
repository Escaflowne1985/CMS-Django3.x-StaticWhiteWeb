# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = 'Configuration 应用 Adminx 后台管理控制配置'

import xadmin
from xadmin import views
from apps.User.models import *  # 载入用户应用模型
from apps.Article.models import *  # 载入文章应用模型
from apps.StatisticalData.models import *


# Adminx 全局设置
class BaseSetting(object):
    # 启用后台主题
    enable_themes = True
    # 切换主题模式
    use_bootswatch = True


# xadmin后台菜单设置
class GlobalSettings(object):
    # 设置站点标题
    site_title = "Python CMS管理后台"
    # 设置站点的页脚
    site_footer = "Mr数据杨制作"
    # 设置默认导航菜单折叠
    menu_style = "accordion"

    def get_site_menu(self):
        UserMenu = {'title': '用户管理', 'icon': 'fa fa-user-circle', 'menus': (
            {'title': '用户列表', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserProfile, 'changelist')},
            {'title': '订阅列表', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserSubscription, 'changelist')},
            {'title': '邮件列表', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserEmailVerifyRecord, 'changelist')},
            {'title': '浏览记录', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserRead, 'changelist')},
            {'title': '收藏记录', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserFav, 'changelist')},
            {'title': '分享记录', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserShare, 'changelist')},
            {'title': '订单记录', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserOrder, 'changelist')},
            {'title': '用户日志', 'icon': 'fa fa-user-o', 'url': self.get_model_url(UserServerLog, 'changelist')},
        )}
        ArticleMenu = {'title': '文章管理', 'icon': 'fa fa-file-text', 'menus': (
            {'title': '文章类别', 'icon': 'fa fa-file-o', 'url': self.get_model_url(ArticleCategory, 'changelist')},
            {'title': '文章栏目', 'icon': 'fa fa-file-o', 'url': self.get_model_url(ArticleItem, 'changelist')},
            {'title': '文章标签', 'icon': 'fa fa-file-o', 'url': self.get_model_url(ArticleTag, 'changelist')},
            {'title': '文章编辑', 'icon': 'fa fa-file-o', 'url': self.get_model_url(ArticleEdit, 'changelist')},
            {'title': '首页文章', 'icon': 'fa fa-file-o', 'url': self.get_model_url(ArticleInfoHome, 'changelist')},
            {'title': '栏目文章', 'icon': 'fa fa-file-o', 'url': self.get_model_url(ArticleInfoItem, 'changelist')},
        )}
        StatisticalDataMenu = {'title': '数据管理', 'icon': 'fa fa-database', 'menus': (
            {'title': '总访问数', 'icon': 'fa fa-bar-chart', 'url': self.get_model_url(VisitTotalNumber, 'changelist')},
            {'title': '每日访问', 'icon': 'fa fa-bar-chart', 'url': self.get_model_url(VisitEveryDayNumber, 'changelist')},
            {'title': 'IP访问模块', 'icon': 'fa fa-bar-chart', 'url': self.get_model_url(VisitIpPart, 'changelist')},
            {'title': 'IP统计', 'icon': 'fa fa-bar-chart', 'url': self.get_model_url(VisitEveryIpCount, 'changelist')},
        )}
        ADMenu = {'title': '广告管理', 'icon': 'fa fa-audio-description', 'menus': (
            {'title': '广告轮播', 'icon': 'fa fa-file-image-o', 'url': self.get_model_url(Banner, 'changelist')},
        )}
        return (
            UserMenu, ArticleMenu, StatisticalDataMenu, ADMenu,
        )


xadmin.site.register(views.CommAdminView, GlobalSettings)  # 全局设置加载
xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册主体风格切换
