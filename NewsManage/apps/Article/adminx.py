# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = 'Articles 应用 Adminx 后台管理控制配置'

import xadmin
from .models import *
from xadmin.layout import *
from NewsManage.settings import *


# 主页通用的更新数据方法
def UpdateHomeData(queryset_model, obj):
    # 文章位置文字描述
    queryset_model.position = [i for i in HOME_POSITION_CHOICES if str(obj.home_position) == i[0]][0][1]
    # 文章位置ID描述
    queryset_model.position_id = obj.home_position
    # 文章基本信息内容
    queryset_model.info_slug = obj.info_slug
    queryset_model.title = obj.title
    queryset_model.category = str(obj.category)
    queryset_model.item = str(obj.item)
    queryset_model.summary = obj.summary
    queryset_model.share_num = obj.share_num
    queryset_model.read_num = obj.read_num
    queryset_model.fav_num = obj.fav_num
    queryset_model.integral_num = obj.integral_num
    queryset_model.cover_jpg = obj.cover_jpg
    queryset_model.cover_url = obj.cover_url
    queryset_model.created_date = obj.created_date
    queryset_model.save()


# 频道通用的更新数据方法
def UpdateItemData(queryset_model, obj):
    queryset_model.info_slug = obj.info_slug
    queryset_model.title = obj.title
    queryset_model.category = str(obj.category)
    queryset_model.item = str(obj.item)
    queryset_model.summary = obj.summary
    queryset_model.share_num = obj.share_num
    queryset_model.read_num = obj.read_num
    queryset_model.fav_num = obj.fav_num
    queryset_model.integral_num = obj.integral_num
    queryset_model.cover_jpg = obj.cover_jpg
    queryset_model.cover_url = obj.cover_url
    queryset_model.created_date = obj.created_date
    queryset_model.save()


class ArticleCategoryAdmin(object):
    list_display = [
        'status_code', 'name', 'item_count',
        'add_user', 'created_date'
    ]
    readonly_fields = [
        'created_date'
    ]
    show_bookmarks = False

    # 统计每个Category下的Item数
    def item_count(self, obj):
        return ArticleItem.objects.filter(category=obj).count()

    # 定义统计列的字段名称
    item_count.short_description = "栏目数量"

    # 默认修改或者新增数据都在add_user中填充当前登陆用户并隐藏
    def instance_forms(self):
        super().instance_forms()
        self.form_obj.initial['add_user'] = self.request.user.id
        self.form_layout = (
            Fieldset(
                None, 'add_user', **{"style": "display:None"}),
        )


class ArticleItemAdmin(object):
    list_display = [
        'status_code', 'category', 'name', "article_count",
        'add_user', 'created_date'
    ]
    readonly_fields = [
        'created_date'
    ]
    show_bookmarks = False

    # 统计每个Item下的文章数量
    def article_count(self, obj):
        return ArticleInfo.objects.filter(item_id=obj).count()

    # 定义统计列的字段名称
    article_count.short_description = "文章数量"

    # 默认修改或者新增数据都在add_user中填充当前登陆用户并隐藏
    def instance_forms(self):
        super().instance_forms()
        self.form_obj.initial['add_user'] = self.request.user.id
        self.form_layout = (
            Fieldset(
                None, 'add_user', **{"style": "display:None"}),
        )


class ArticleTagAdmin(object):
    list_display = [
        'status_code', 'name',
        'add_user', 'created_date'
    ]
    readonly_fields = [
        'created_date'
    ]
    show_bookmarks = False

    # 默认修改或者新增数据都在add_user中填充当前登陆用户并隐藏
    def instance_forms(self):
        super().instance_forms()
        self.form_obj.initial['add_user'] = self.request.user.id
        self.form_layout = (
            Fieldset(
                None, 'add_user', **{"style": "display:None"}),
        )


class ArticleEditAdmin(object):
    list_display = [
        'status_code',
        'title', 'category', 'item',
        'article_author', 'audit_user',
        'created_date'
    ]
    style_fields = {"content": "ueditor", "storage_content": "ueditor"}
    show_bookmarks = False
    list_per_page = 30
    readonly_fields = [
        "info_slug", "detail_slug", "storage_slug",
        "share_num", "read_num", "fav_num",
        "created_date"
    ]

    # 拥有审核权限逻辑，自动填充审核用户id，隐藏某些字段
    def instance_forms(self):
        super().instance_forms()
        if self.request.user.user_role in USER_IDENTITY_LIST:
            self.form_obj.initial['article_author'] = self.request.user.id
            self.form_layout = (
                Fieldset(None,
                         'article_author', 'detail_slug', 'storage_slug',
                         **{"style": "display:None"}),
                TabHolder(
                    Tab('基本信息I',
                        Fieldset(("基本信息"),
                                 Row('info_slug', 'created_date'),
                                 Field('title', css_class="extra"),
                                 'category', 'item',
                                 Row('cover_jpg', 'cover_url'),
                                 ),
                        Fieldset(("文章位置"),
                                 'home_position', 'item_position',
                                 ),
                        Fieldset(("其他信息"),
                                 'ai_type', 'key_words', 'tags', 'source', 'source_url'
                                 ),
                        ),
                    Tab('文章详情C',
                        Fieldset(("文章编辑"),
                                 Field('summary', css_class="extra"),
                                 Field('content'),
                                 ),
                        ),
                    Tab('文章附件S',
                        Fieldset(("文章数据"),
                                 Field("integral_num", "storage_content"),
                                 ),
                        ),
                    Tab('文章数据D',
                        Fieldset(("审核情况"),
                                 Field("status", "article_author", "audit_user"),
                                 ),
                        Fieldset(("文章数据"),
                                 Field("province", "city"),
                                 Field("read_num", "share_num", "fav_num"),
                                 ),
                        ),
                )
            )
        else:
            # 非审核权限逻辑，自动填充编辑用户id，审核字段未None,隐藏审核字段
            self.form_obj.initial['article_author'] = self.request.user.id
            self.form_obj.initial['audit_user'] = None
            self.form_layout = (
                Fieldset(None,
                         'article_author', 'detail_slug', 'storage_slug',
                         **{"style": "display:None"}),
                TabHolder(
                    Tab('基本信息I',
                        Fieldset(("基本信息"),
                                 Row('info_slug', 'created_date'),
                                 Field('title', css_class="extra"),
                                 'category', 'item',
                                 Row('cover_jpg', 'cover_url'),
                                 ),
                        Fieldset(("文章位置"),
                                 'home_position', 'item_position',
                                 ),
                        Fieldset(("其他信息"),
                                 'ai_type', 'key_words', 'tags', 'source', 'source_url'
                                 ),
                        ),
                    Tab('文章详情C',
                        Fieldset(("文章编辑"),
                                 Field('summary', css_class="extra"),
                                 Field('content'),
                                 ),
                        ),
                    Tab('文章附件S',
                        Fieldset(("文章数据"),
                                 Field("integral_num", "storage_content"),
                                 ),
                        ),
                    Tab('文章数据D',
                        Fieldset(("审核情况"),
                                 Field("status", "article_author", "audit_user"),
                                 ),
                        Fieldset(("文章数据"),
                                 Field("province", "city"),
                                 Field("read_num", "share_num", "fav_num"),
                                 ),
                        ),
                )
            )

    # 非拥有审核权限用户智能看到自己创建的数据信息
    def queryset(self):
        if self.request.user.user_role not in USER_IDENTITY_LIST:
            qs = super(ArticleEditAdmin, self).queryset()
            return qs.filter(article_author=self.request.user.id)
        else:
            qs = super(ArticleEditAdmin, self).queryset()
            return qs.filter()

    # 这里重写save_model同步数据
    def save_models(self):
        # 保存内容审核部分
        if self.request.user.user_role in USER_IDENTITY_LIST:
            obj = self.new_obj
            obj.save()
        else:
            obj = self.new_obj
            obj.status = "0"
            obj.save()

        # 获取数据更新方式方法，获取结果为url中的add 或者 update
        request_method = self.request.path.split("/")[-2]

        # 主页展示内容，编辑条件主页有位置切审核通过
        if obj.home_position != "0" and obj.status == "1":
            # 判断文章执行动作 add表示新增，update表示更新
            if request_method == 'add':
                queryset_model = ArticleInfoHome()
                UpdateHomeData(queryset_model, obj)
            if request_method == 'update':
                try:
                    queryset_model = ArticleInfoHome.objects.filter(info_slug=obj.info_slug)[0]
                    UpdateHomeData(queryset_model, obj)
                except IndexError as e:
                    queryset_model = ArticleInfoHome()
                    UpdateHomeData(queryset_model, obj)

        # 二级栏目内容，编辑条件主页有位置切审核通过
        if obj.item_position == "1" and obj.status == "1":
            # 判断文章执行动作 add表示新增，update表示更新
            if request_method == 'add':
                queryset_model = ArticleInfoItem()
                UpdateItemData(queryset_model, obj)
            if request_method == 'update':
                try:
                    queryset_model = ArticleInfoItem.objects.filter(info_slug=obj.info_slug)[0]
                    UpdateItemData(queryset_model, obj)
                except IndexError as e:
                    queryset_model = ArticleInfoItem()
                    UpdateItemData(queryset_model, obj)


class ArticleInfoHomeAdmin(object):
    list_display = [
        'info_slug', 'module_top',
        'title', 'category', 'item',
        'position',
    ]
    search_fields = [
        'title'
    ]
    show_bookmarks = False
    list_per_page = 30

    # 仅允许管理人员进行置顶操作
    def get_readonly_fields(self):
        if self.request.user.user_role in USER_IDENTITY_LIST:
            fields = [
                'info_slug', 'position', 'position_id',
                'title', 'category', 'item',
                'summary', 'share_num', 'read_num', 'fav_num', 'integral_num',
                'cover_jpg', 'cover_url',
            ]
            return fields
        else:
            fields = [f.name for f in self.model._meta.fields]
            return fields


class ArticleInfoItemAdmin(object):
    list_display = [
        'info_slug', 'title', 'category', 'item'
    ]
    show_bookmarks = False
    list_per_page = 30
    search_fields = [
        'title'
    ]

    # 全部字段只读
    def get_readonly_fields(self):
        fields = [f.name for f in self.model._meta.fields]
        return fields


class BannerAdmin(object):
    list_display = ['name', 'url']
    show_bookmarks = False


xadmin.site.register(ArticleCategory, ArticleCategoryAdmin)
xadmin.site.register(ArticleItem, ArticleItemAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
xadmin.site.register(ArticleEdit, ArticleEditAdmin)
xadmin.site.register(ArticleInfoHome, ArticleInfoHomeAdmin)
xadmin.site.register(ArticleInfoItem, ArticleInfoItemAdmin)
xadmin.site.register(Banner, BannerAdmin)
