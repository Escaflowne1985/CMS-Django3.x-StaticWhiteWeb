# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '表单配置选择文件'

import datetime
import time

"""User应用部分"""
# 性别选择
GENDER_CHOICES = (
    ("Male", "男性"),
    ("Female", "女性"),
    ("Undefined", "未定义")
)
# 身份选择
ROLE_CHOICES = (
    ("Root", "超级管理员"),
    ("EditUser", "编辑"),
    ("ReviewUser", "审核"),
    ("WebsiteUsers", "网站用户"),
    ("Tourist", "游客")
)

"""文章应用部分"""
# 日期函数 用于制作上传图片和文件路径
time_y = (time.strftime("%Y"))
time_m = (time.strftime("%m"))


# 设置默认时间戳转换Str生成文章Slug
def default_time():
    return datetime.datetime.now().strftime("%Y%m%d%X").replace(":", "")


# 用户身份管理身份，后台编辑权限设置，非设置身份不可修改内容
USER_IDENTITY_LIST = ["Root", "ReviewUser"]

# 文章状态
CONTENT_STATUS_CHOICES = (
    ("0", "未审核"),
    ("1", "已审核"),
    ("2", "审核不通过")
)
CONTENT_STATUS_COLOUR = (
    ("0", "yellow"),
    ("1", "green"),
    ("2", "red")
)

# 文章类别标签
TAG_TYPE_CHOICES = (
    ("001", "文章二级栏目1"),
    ("002", "文章二级栏目2"),
    ("003", "文章二级栏目3"),
    ("004", "文章二级栏目4"),
)

# 内容位置设置
HOME_POSITION_CHOICES = (
    ("0", "非首页显示"),
    ("1", "最新内容"),
    ("2", "热门内容"),
    ("3", "浏览最多"),
    ("4", "转发最多"),
    ("5", "收藏最多"),
    ("6", "内容滚动推荐"),
    ("7", "大图置顶轮播"),
)

# 是否在栏目列表中可见
ITEM_POSITION_CHOICES = (
    ("0", "栏目中不显示"),
    ("1", "栏目中显示数据"),
)

# 内容是否置顶
MODULE_CHOICES = (
    ("0", "不置顶"),
    ("1", "置顶"),
)
