# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'Articles 应用 文章模型配置'

from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
from django.contrib.auth import get_user_model
from apps.Configuration.config_choose import *
from django.utils.html import format_html

User = get_user_model()  # 加载用户设置信息


# 文章一级大类
class ArticleCategory(models.Model):
    # 通用管理部分
    add_user = models.ForeignKey(User, related_name='ACAddUser', on_delete=models.CASCADE,verbose_name='数据录入用户', help_text="数据录入系统用户")
    status = models.CharField(choices=CONTENT_STATUS_CHOICES, max_length=1, default=0,verbose_name='使用状态', help_text="使用状态，默认未审核")
    created_date = models.DateTimeField(default=timezone.now,verbose_name='数据创建时间', help_text='数据创建时间，使用默认的系统时间')
    # 模型私有部分
    name = models.CharField(max_length=30,verbose_name='大类名称', help_text="文章一级大类名称")

    # 自定义审核状态和不同状态字体颜色
    def status_code(self):
        color_code = [i[1] for i in CONTENT_STATUS_COLOUR if i[0] == self.status][0]
        status = [i[1] for i in CONTENT_STATUS_CHOICES if i[0] == self.status][0]
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            status,
        )

    status_code.short_description = '审核状态'

    class Meta:
        verbose_name = '文章一级大类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章二级栏目
class ArticleItem(models.Model):
    # 通用管理部分
    add_user = models.ForeignKey(
        User, related_name='AIAddUser', on_delete=models.CASCADE,
        verbose_name='数据录入用户', help_text="数据录入系统用户"
    )
    status = models.CharField(
        choices=CONTENT_STATUS_CHOICES, max_length=1, default=0,
        verbose_name='使用状态', help_text="使用状态，默认未审核"
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='数据创建时间', help_text='数据创建时间，使用默认的系统时间'
    )
    # 模型私有部分
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.CASCADE, related_name='ArticleItemCategory',
        verbose_name="栏目所属一级大类", help_text="栏目所属一级大类，若没有请在文章类别管理中创建"
    )
    name = models.CharField(
        max_length=30,
        verbose_name="栏目名称", help_text="文章二级栏目名称"
    )

    # 自定义审核状态和不同状态字体颜色
    def status_code(self):
        color_code = [i[1] for i in CONTENT_STATUS_COLOUR if i[0] == self.status][0]
        status = [i[1] for i in CONTENT_STATUS_CHOICES if i[0] == self.status][0]
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            status,
        )

    status_code.short_description = '审核状态'

    class Meta:
        verbose_name = '文章二级栏目管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class ArticleTag(models.Model):
    # 通用管理部分
    add_user = models.ForeignKey(
        User, related_name='ATAddUser', on_delete=models.CASCADE,
        verbose_name='数据录入用户', help_text="数据录入系统用户"
    )
    status = models.CharField(
        choices=CONTENT_STATUS_CHOICES, max_length=1, default=0,
        verbose_name='使用状态', help_text="使用状态，默认未审核"
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='数据创建时间', help_text='数据创建时间，使用默认的系统时间'
    )
    # 模型私有部分
    name = models.CharField(
        max_length=50,
        verbose_name='标签名称', help_text="文章标签中文名称"
    )

    # 自定义审核状态和不同状态字体颜色
    def status_code(self):
        color_code = [i[1] for i in CONTENT_STATUS_COLOUR if i[0] == self.status][0]
        status = [i[1] for i in CONTENT_STATUS_CHOICES if i[0] == self.status][0]
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            status,
        )

    status_code.short_description = '审核状态'

    class Meta:
        verbose_name = '文章标签管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章基本信息
class ArticleInfo(models.Model):
    # 通用管理部分
    article_author = models.ForeignKey(
        User,
        related_name='AIAuthor', on_delete=models.CASCADE,
        verbose_name='文章作者', help_text="数据录入系统用户"
    )
    audit_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='AIAudit',
        verbose_name='审核用户', help_text="数据录入系统用户",
        blank=True, null=True
    )
    status = models.CharField(
        choices=CONTENT_STATUS_CHOICES, max_length=1, default=0,
        verbose_name='审核状态', help_text="默认未审核，超级用户和编辑有权限审核"
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='数据创建时间', help_text='数据创建时间，使用默认的系统时间'
    )
    # 模型私有部分
    home_position = models.CharField(
        choices=HOME_POSITION_CHOICES,
        max_length=1, default=0,
        verbose_name='文章显示位置', help_text="默认非主页显示，若没有请在config_choose中添加"
    )
    item_position = models.CharField(
        choices=ITEM_POSITION_CHOICES,
        max_length=1, default=0,
        verbose_name='栏目是否可见', help_text="默认栏目中不显示"
    )
    title = models.CharField(
        max_length=100, default="",
        verbose_name='文章标题', help_text="文章标题，最多使用100个字符"
    )
    category = models.ForeignKey(
        ArticleCategory,
        related_name='ArticleInfoCategory', on_delete=models.CASCADE,
        verbose_name="文章一级类别", help_text="文章所属的一级大类"
    )
    item = models.ForeignKey(
        ArticleItem,
        related_name='ArticleInfoItem', on_delete=models.CASCADE,
        verbose_name="文章二级栏目", help_text="文章所属的二级栏目"
    )
    info_slug = models.SlugField(
        default=default_time,
        verbose_name='文章slug标签', help_text='slug按照时间戳自动生成',
        primary_key=True
    )
    ai_type = models.CharField(
        max_length=20,
        verbose_name='算法分类', help_text="算法API接口的文章分类",
        null=True, blank=True
    )
    summary = models.CharField(
        max_length=200, default="",
        verbose_name='摘要', help_text="文章标题，最多使用200个字符",
        null=True, blank=True
    )
    key_words = models.CharField(
        max_length=100, default='Mr数据杨,CMS管理平台',
        verbose_name='关键词', help_text="文章关键词，格式：默认样式。使用,分割。最多使用100个字符",
        null=True, blank=True
    )
    tags = models.ManyToManyField(
        ArticleTag, related_name='ArticleInfoTags',
        verbose_name='文章中文标签', help_text="文章标签中文名称",
        blank=True
    )
    cover_jpg = models.ImageField(
        upload_to='ArticleCover/%Y/%m', default='ArticleCover/default.png',
        verbose_name='文章封面图片', help_text="若未上传封面，则使用默认图片",
        null=True, blank=True
    )
    cover_url = models.URLField(
        max_length=500,
        verbose_name='文章封面链接', help_text="爬虫抓取的文章原文封面url链接",
    )
    source = models.CharField(
        max_length=50, default="原创",
        verbose_name='原文来源网站', help_text="爬虫抓取的文章来源网站信息，若不存在则标记未原创",
        null=True, blank=True
    )
    source_url = models.CharField(
        max_length=500, default="原创",
        verbose_name="原文来源链接", help_text="爬虫抓取的文章来源的url链接，若不存在则标记未原创",
        null=True, blank=True
    )
    province = models.CharField(
        max_length=20, default="全国",
        verbose_name='省市区域', help_text="用于标记文章显示的省级区域，默认全国",
        blank=True
    )
    city = models.CharField(
        max_length=20, default="全地区",
        verbose_name='城市区域', help_text="用于标记文章显示的市级区域，默认全地区",
        blank=True
    )
    share_num = models.IntegerField(
        default=0,
        verbose_name='文章转发数', help_text="用户转发文章数量"
    )
    read_num = models.IntegerField(
        default=0,
        verbose_name='文章浏览数', help_text="用户浏览文章数量"
    )
    fav_num = models.IntegerField(
        default=0,
        verbose_name='文章收藏数', help_text="用户收藏文章数量"
    )
    integral_num = models.IntegerField(
        default=0,
        verbose_name="文章积分", help_text="阅读文章需要的积分数量，默认0"
    )

    # 自定义审核状态和不同状态字体颜色
    def status_code(self):
        color_code = [i[1] for i in CONTENT_STATUS_COLOUR if i[0] == self.status][0]
        status = [i[1] for i in CONTENT_STATUS_CHOICES if i[0] == self.status][0]
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            status,
        )

    status_code.short_description = '审核状态'

    class Meta:
        verbose_name = '文章基本信息管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文章详情信息
class ArticleDetail(models.Model):
    # 模型私有部分
    detail_slug = models.SlugField(
        default=default_time,
        verbose_name='文章slug标签', help_text='slug按照时间戳自动生成',
        primary_key=True
    )
    content = UEditorField(
        '文章正文', height=400, width=800, default='', toolbars='besttome',
        imagePath="ArticleDetailImages/{}/{}/".format(time_y, time_m),
        filePath="ArticleDetailFile/{}/{}/".format(time_y, time_m),
        null=True, blank=True
    )

    class Meta:
        verbose_name = '文章详情管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.detail_slug


# 文章附件购买储链接模型
class ArticleStorage(models.Model):
    # 模型私有部分
    storage_slug = models.SlugField(
        default=default_time,
        verbose_name='文章slug标签', help_text='slug按照时间戳自动生成',
        primary_key=True
    )
    storage_content = UEditorField(
        '文章附件信息', default="链接失效请点击：我的文章-我的后台联系管理员",
        height=400, width=800, toolbars='besttome',
        null=True, blank=True
    )

    class Meta:
        verbose_name = '文章附件管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.storage_slug


# 拼接内容基本信息和详情模型（用于整体后台编辑）
class ArticleEdit(ArticleInfo, ArticleDetail, ArticleStorage):
    class Meta:
        verbose_name = '文章内容编辑'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 主页文章信息模型（用于主页内容快速加载展示）
class ArticleInfoHome(models.Model):
    info_slug = models.SlugField(
        default=default_time,
        verbose_name='文章slug',
    )
    position = models.CharField(
        max_length=50, default="",
        verbose_name='主页展示位置名称', help_text="主页展示位置名称"
    )
    position_id = models.CharField(
        max_length=50, default="",
        verbose_name='主页展示位置ID', help_text="主页展示位置ID编号"
    )
    module_top = models.CharField(
        choices=MODULE_CHOICES, max_length=1, default=0,
        verbose_name='文章置顶标识', help_text="文章是否所在位置置顶，默认不置顶"
    )
    title = models.CharField(
        max_length=100, default="",
        verbose_name='文章标题', help_text="文章标题，最多使用100个字符"
    )
    category = models.CharField(
        max_length=50, default="",
        verbose_name="文章一级类别", help_text="文章所属的一级大类"
    )
    item = models.CharField(
        max_length=50, default="",
        verbose_name="文章二级栏目", help_text="文章所属的二级栏目"
    )
    summary = models.CharField(
        max_length=200,
        verbose_name='摘要', help_text="文章标题，最多使用200个字符",
    )
    share_num = models.IntegerField(
        default=0,
        verbose_name='文章转发数', help_text="用户转发文章数量"
    )
    read_num = models.IntegerField(
        default=0,
        verbose_name='文章浏览数', help_text="用户浏览文章数量"
    )
    fav_num = models.IntegerField(
        default=0,
        verbose_name='文章收藏数', help_text="用户收藏文章数量"
    )
    integral_num = models.IntegerField(
        default=0,
        verbose_name="文章积分", help_text="阅读文章需要的积分数量，默认0"
    )
    cover_jpg = models.ImageField(
        verbose_name='文章封面图片', help_text="若未上传封面，则使用默认图片",
        null=True, blank=True
    )
    cover_url = models.URLField(
        max_length=500,
        verbose_name='文章封面链接', help_text="爬虫抓取的文章原文封面url链接",
        null=True, blank=True
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='数据创建时间', help_text='数据创建时间，使用默认的系统时间'
    )

    class Meta:
        verbose_name = '主页文章数据管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 栏目内容模型（用于二级分类内容快速加载展示）
class ArticleInfoItem(models.Model):
    info_slug = models.SlugField(
        default=default_time,
        verbose_name='文章slug标签', help_text='slug按照时间戳自动生成',
    )
    title = models.CharField(
        max_length=100, default="",
        verbose_name='文章标题', help_text="文章标题，最多使用100个字符"
    )
    category = models.CharField(
        max_length=50, default="",
        verbose_name="文章一级类别", help_text="文章所属的一级大类"
    )
    item = models.CharField(
        max_length=50, default="",
        verbose_name="文章二级栏目", help_text="文章所属的二级栏目"
    )
    summary = models.CharField(
        max_length=200,
        verbose_name='摘要', help_text="文章标题，最多使用200个字符",
    )
    share_num = models.IntegerField(
        default=0,
        verbose_name='文章转发数', help_text="用户转发文章数量"
    )
    read_num = models.IntegerField(
        default=0,
        verbose_name='文章浏览数', help_text="用户浏览文章数量"
    )
    fav_num = models.IntegerField(
        default=0,
        verbose_name='文章收藏数', help_text="用户收藏文章数量"
    )
    integral_num = models.IntegerField(
        default=0,
        verbose_name="文章积分", help_text="阅读文章需要的积分数量，默认0"
    )
    cover_jpg = models.ImageField(
        verbose_name='文章封面图片', help_text="若未上传封面，则使用默认图片",
        null=True, blank=True
    )
    cover_url = models.URLField(
        max_length=500,
        verbose_name='文章封面链接', help_text="爬虫抓取的文章原文封面url链接",
        null=True, blank=True
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='数据创建时间', help_text='数据创建时间，使用默认的系统时间'
    )

    class Meta:
        verbose_name = '栏目文章数据管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 图片轮播内容模型
class Banner(models.Model):
    name = models.CharField(
        max_length=50, default="",
        verbose_name='Banner名称', help_text="轮播图名称"
    )
    type = models.CharField(
        max_length=50, default="",
        verbose_name='Banner类别', help_text="轮播图类别"
    )
    info = models.CharField(
        max_length=50, default="",
        verbose_name='Banner介绍', help_text="轮播图文字介绍"
    )
    image = models.ImageField(
        upload_to='BannerImager/%Y/%m',
        verbose_name='轮播图图片', help_text="轮播图像素大小1920x768",
        blank=True,
    )
    url = models.URLField(
        default="www.baidu.com",
        verbose_name='轮播图链接', help_text="轮播图点击跳转url链接"
    )

    class Meta:
        verbose_name = 'Banner轮播图管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
