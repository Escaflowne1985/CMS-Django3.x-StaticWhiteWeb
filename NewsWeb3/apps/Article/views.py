# coding:utf-8
__author__ = 'Mr数据杨'
__explain__ = '内容功能视图,部署统一修改BaseUrl'

import random
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from apps.utils.RequestTools import *
# 加载settings中设置的API网址和端口号
from NewsWeb3.settings import *
import json

# 设置API基本参数
# 设置分页
PAGESIZE = 10

# 文章应用路由
ArticleCategoryUrl = ApiBaseUrl + '/ArticleSettings/ArticleCategory/'
ArticleItemUrl = ApiBaseUrl + '/ArticleSettings/ArticleItem/'
ArticleTagUrl = ApiBaseUrl + '/ArticleSettings/ArticleTag/'
ArticleTagTypeUrl = ApiBaseUrl + '/ArticleSettings/ArticleTagType'
ArticleInfoUrl = ApiBaseUrl + '/ArticleSettings/ArticleInfo/'
ArticleDetailUrl = ApiBaseUrl + '/ArticleSettings/ArticleDetail/'
ArticleStorageLinkUrl = ApiBaseUrl + '/ArticleSettings/ArticleStorageLink/'
ArticleInfoHomeListUrl = ApiBaseUrl + '/ArticleSettings/ArticleInfoHomeList/'
ArticleInfoItemListUrl = ApiBaseUrl + '/ArticleSettings/ArticleInfoItemList/'
# 轮播图路由
MyBannerListUrl = ApiBaseUrl + '/ArticleSettings/MyBannerList/'
# 统计数据路由
VisitTotalNumberListUrl = ApiBaseUrl + '/StatisticalDataSettings/VisitTotalNumber/'
# VisitEveryDayNumberListUrl = ApiBaseUrl + '/GeneralDataSettings/VisitEveryDayNumberList/'
VisitIpPartListUrl = ApiBaseUrl + '/StatisticalDataSettings/VisitIpPart/'
# VisitEveryIpCountListUrl = ApiBaseUrl + '/GeneralDataSettings/VisitEveryIpCountList/'
# 用户路由
UserProfileListUrl = ApiBaseUrl + '/UserSettings/UserProfile/'
UserSubscriptionListUrl = ApiBaseUrl + '/UserSettings/UserSubscription/'
UserFavUrl = ApiBaseUrl + '/UserSettings/UserFav/'
UserReadListUrl = ApiBaseUrl + '/UserSettings/UserRead/'
UserOrderListUrl = ApiBaseUrl + '/UserSettings/UserOrder/'


# 设置全局数据
def GlobalInitArticle(request):
    # 文章一级大类列表
    ArticleCategoryList = GetData(ArticleCategoryUrl)
    # 文章二级栏目列表
    ArticleItemUrlList = GetData(ArticleItemUrl)
    # 轮播图数据列表
    MyBannerListUrlList = GetData(MyBannerListUrl)
    # 主页 7 个板块显示的内容数据列表
    ArticleInfoHomeListUrlList = GetData(ArticleInfoHomeListUrl)
    return locals()


# 主页Home视图
def HomePage(request):
    # 通过Session获取用户登陆信息
    UserInfo = GetUserInfo(UserProfileListUrl, request)
    # 记录访问的IP信息数据
    VisitIpPost(VisitIpPartListUrl, request, "访问主页")

    return render(request, 'articles/HomePage.html', locals())


# 用户订阅功能
def UserSubscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # 订阅邮件提交
        msg = UserSubscriptionPost(UserSubscriptionListUrl, email)
        return render(request, 'articles/HomePage.html', locals())


# 获得二级栏目内容列表
def GetArticleItemInfo(request, category, item, page):
    # 获取page信息，首页跳转过来默认第一页
    page = page
    # 通过Session获取用户登陆信息
    UserInfo = GetUserInfo(UserProfileListUrl, request)

    # # 根据栏目和频道信息提取对应的Tag标签，提供快速搜索
    # TagList = Tag_list_data(category, item)

    # 总页数、遍历的页数、栏目的url
    max_page, pageRange, ArticleList, next_page_num, previous_pag_num, page = TurnPage(
        request=request,  # request
        Url=ArticleInfoItemListUrl,  # 数据API路由
        page=page,  # 访问的数据页码信息
        search_type="GetArticleItemInfo",  # 访问的数据类型
        category=category,  # 跳转内容的一级大类
        item=item  # 跳转内容的二级栏目
    )
    # 文章一级大类 category / 文章二级栏目 item
    category = category
    item = item

    # 记录访问的IP信息数据
    VisitIpPost(VisitIpPartListUrl, request, "二级栏目浏览")
    return render(request, 'articles/ArticleList.html', locals())


# Tag选择列表数据
def Tag_list_data(category_name, item_name):
    # 获取标签的类别信息
    type_dict = GetData(ArticleTagTypeUrl)
    # {'文章标签类别1': '001', '文章标签类别2': '002', '文章标签类别3': '003', '文章标签类别4': '004'}
    # 提取对应item的num数字
    type_num = type_dict[item_name]

    # 默认tag取3个
    TagList = GetData(
        (ArticleTagUrl + "?tag_type={}".format(type_num))
    )
    TagList = random.sample(TagList, 3)

    return TagList


# 搜索功能 关键词、标签搜索搜索
def GetArticleSearchInfoGet(request, search_data, page):
    # 通过Session获取用户登陆信息
    UserInfo = GetUserInfo(UserProfileListUrl, request)
    # GET数据查询方法
    if request.method == 'GET':
        # 获取前端提交的搜索数据类型
        search_type = "word_search"
        # 获取前端提交的搜索数据内容
        search_data = search_data
        # 默认的page数量
        page = page
        # 获取文章列表 tag_search
        max_page, pageRange, ArticleList, next_page_num, previous_pag_num, page = TurnPage(
            request=request,
            Url=ArticleInfoUrl,
            page=page,
            search_type=search_type,
            search_data=search_data
        )  # 总页数、遍历的页数、栏目的url
        # print("1:", next_page_num, "2:", previous_pag_num, "3:", page)
        VisitIpPost(VisitIpPartListUrl, request, search_type + "搜索")
        return render(request, 'articles/SearchArticleList.html', locals())

    # 记录访问的IP信息数据
    VisitIpPost(VisitIpPartListUrl, request, "进入搜索页")
    return render(request, 'articles/Search.html', locals())


# 搜索功能 关键词、标签搜索搜索
def GetArticleSearchInfoPost(request):
    # 通过Session获取用户登陆信息
    UserInfo = GetUserInfo(UserProfileListUrl, request)

    # POST提交数据查询方法
    if request.method == 'POST':
        # 获取前端提交的搜索数据类型
        search_type = request.POST.get('search_type')
        # 获取前端提交的搜索数据内容
        search_data = request.POST.get('search_data')
        # 默认的page数量
        page = int(request.GET.get('page', 1))
        # 判断搜索内容是否为空
        if search_data == "":
            return render(request, "articles/Search.html", status=500)
        # 获取文章列表 word_search 总页数、遍历的页数、栏目的url
        max_page, pageRange, ArticleList, next_page_num, previous_pag_num, page = TurnPage(
            request=request,
            Url=ArticleInfoUrl,
            page=page,
            search_type=search_type,
            search_data=search_data
        )

        # 记录访问的IP信息数据
        VisitIpPost(VisitIpPartListUrl, request, search_type + "搜索")
        return render(request, 'articles/SearchArticleList.html', locals())

    # 记录访问的IP信息数据
    VisitIpPost(VisitIpPartListUrl, request, "进入搜索页")
    return render(request, 'articles/Search.html', locals())


# 获得对应文章的详情,其中包括用户文章阅读记录，文章收藏记录
def GetArticleDetail(request, info_slug):
    # 获取文章基础信息
    ArticleInfo = GetData(urljoin(ArticleInfoUrl, info_slug))
    # 获取文章的标签tag
    tag_list = ArticleInfo["tags"]
    # 通过Session获取用户登陆信息
    UserInfo = GetUserInfo(UserProfileListUrl, request)
    # 通过Tag进行的相关推荐(这里暂时没想好更优秀的对应推荐算法机制)
    info_tag_name = ArticleInfo["tags"][0]["name"]
    TagRecommendList = GetData(
        (ArticleInfoUrl + "?tag={}".format(info_tag_name))
    )['results']
    """
    # 判断是否有JWT_Token，通过JWT_Token阅读文章正文(暂时不使用)
    if request.session["jwt_token"]:
        jwt_token = request.session["jwt_token"]
        # 通过JWT方式获取文章正文内容
        detail_content = json.loads(GetArticleContent(ArticleDetailUrl, article_slug, jwt_token))["detail_content"]
    else:
        detail_content = "登陆后才可以浏览"
    """

    # 通过API拼接文章Slug的方式获取文章正文和网盘信息链接内容
    detail_content = GetData(ArticleDetailUrl + info_slug)["content"]
    link_content = json.loads(GetArticleStorageLink(ArticleStorageLinkUrl, info_slug).text)

    # 判断文章是否是0积分的免费资源
    if ArticleInfo["integral_num"] == 0:
        exchange_data = link_content
    else:
        try:
            # 获取username数据
            username = UserInfo["username"]
            # 通过API拼接订单中的用户名获取兑换的信息内容
            exchange_info = json.loads(GetArticleBuyInfo(UserOrderListUrl, username, info_slug).text)
            # 如果有购买信息 就显示内容
            if exchange_info:
                exchange_data = link_content
            else:
                exchange_data = "not free"
        except:
            UserInfo = None

    # 根据登陆状态判断 用户收藏行为
    if UserInfo is not None:
        # 获取username数据
        username = UserInfo["username"]
        # 通过API写入用户阅读记录数据
        UserFavShareReadPost(UserReadListUrl, username, info_slug)
        # 获取用户是否收藏过该文章
        has_fav = GetData(UserFavUrl + "?username={}&info_slug={}".format(username, info_slug))
        # 记录访问的IP信息数据
        VisitIpPost(VisitIpPartListUrl, request, "主页")
        return render(request, 'articles/ArticleDetail.html', locals())

    # 记录访问的IP信息数据 无登陆状态返回
    VisitIpPost(VisitIpPartListUrl, request, "主页")

    return render(request, 'articles/ArticleDetail.html', locals())
