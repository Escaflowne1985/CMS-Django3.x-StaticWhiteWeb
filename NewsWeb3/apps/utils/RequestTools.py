# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = '访问后端API数据获取实用程序'

from urllib import parse
from urllib.parse import urljoin
import datetime
import time
import json
import requests
import re
from django.contrib.auth.hashers import make_password

# 设置注册post请求headers
headers = {
    'content-type': 'application/json'
}


# 访问数据API接口解析json数据
def GetData(url_, data=None):
    try:
        if data:
            data = '?' + parse.urlencode(data)
            url = urljoin(url_, data)
            html = requests.get(url)
        else:
            html = requests.get(url_)
        return_data = json.loads(html.text)

    except Exception as e:
        return_data = {'result': e, 'code': e, 'msg': '请求api数据错误！', 'data': '{}', 'redirect_url': ''}
    return return_data


# 获取用户JWT的Token
def UserJWTTokenPost(Url, username, password):
    user_data = {
        "username": username,
        "password": password
    }
    respond = requests.post(Url, headers=headers, data=json.dumps(user_data))
    return json.loads(respond.text)["token"]


# 新增用户行为日志到API服务器
def UserServerLogPost(Url, username, operation_type, content, status, remark):
    # 构建用户行为日志字典
    log_data = {
        "user": username,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "type": operation_type,
        "content": content,
        "status": status,
        "remark": remark,
    }
    requests.post(Url, headers=headers, data=json.dumps(log_data))


# 新增用户信息
def RegisterUserProfile(Url, username, email, mobile, password):
    # 构建用户注册数据字典
    register_user_data = {
        'username': username,
        'email': email,
        'mobile': mobile,
        'password': make_password(password, None, 'pbkdf2_sha256'),
        'nick_name': '网站用户' + str(int(time.time())),
        'is_active': 0,
    }
    # 向服务器注册用户
    requests.post(Url, headers=headers, data=json.dumps(register_user_data))


# 提交用户Token信息
def UserInfoTokenPost(Url, username, password):
    # 构建用户修改密码字典
    active_user_data = {
        "username": username,
        "password": password,
    }
    # 向服务器post用户信息返回用户数据token
    register_state = requests.post(
        Url,
        headers=headers,
        data=json.dumps(active_user_data)
    )
    username = json.loads(register_state.text)["username"]
    jwt_token = json.loads(register_state.text)["token"]
    return_data = {
        "username": username,
        "jwt_token": jwt_token
    }
    return return_data


# 更改用户密码（重置）
def UserProfileResetPasswordPut(Url, username, password):
    # 构建用户修改密码字典
    reset_user_data = {
        'username': username,
        'password': make_password(password, None, 'pbkdf2_sha256'),
    }
    # 向服务器更新密码
    url_ = Url + username + "/"
    result = requests.patch(
        url_,
        headers=headers,
        data=json.dumps(reset_user_data)
    )


# 更新用户激活状态
def UserProfileActivePut(Url, username, password):
    # 构建用户激活状态字典
    active_user_data = {
        "username": username,
        "password": make_password(password, None, 'pbkdf2_sha256'),
        "is_active": 1
    }
    # 向服务器更新密码
    url_ = Url + username + "/"
    result = requests.put(
        url_,
        headers=headers,
        data=json.dumps(active_user_data)
    )


# 新增收藏、分享、浏览数据信息
def UserFavShareReadPost(Url, username, info_slug, share_type=None):
    # 构建用户注册数据字典
    user_article_data = {
        'username': username,
        'info_slug': info_slug,
    }
    if share_type:
        user_article_data = {
            'username': username,
            'info_slug': info_slug,
            'share_type': share_type
        }
    # 向服务器注册用户
    result = requests.post(Url, headers=headers, data=json.dumps(user_article_data))


# 获取文章正文
def GetArticleContent(Url, info_slug, jwt_token):
    jwt_headers = {
        'content-type': 'application/json',
        'Authorization': 'JWT ' + jwt_token
    }
    return requests.get(Url + info_slug, headers=jwt_headers).text


# 内容购买查询
def GetArticleBuyInfo(Url, username, info_slug):
    url = Url + "?username={}&info_slug={}".format(username, info_slug)
    return requests.get(url)


# 获取内容存储链接
def GetArticleStorageLink(Url, info_slug):
    url = Url + info_slug
    return requests.get(url)


# 计算page方法所有内容列表只显示5页50条数据，如果page数量大于5则返回5
def CountPage(page):
    page = 5 if page > 5 else page
    return page


# 正则表达式获取page的数字
def RePage(url):
    try:
        pattern = re.compile(r'(?<=page=)\d+\.?\d*')
        return pattern.findall(url)[0]
    except:
        return ""


# 页码计算和翻页功能
def TurnPage(request, Url, page, search_type=None, search_data=None, category=None, item=None):
    # 确定最大的页码数防止出错
    global pageRange
    # 获取需要浏览的page页码数字
    page = CountPage(page)
    # 设定最大页码数
    max_page = 5

    """ 根据不同的类型进行列表页的数据显示 """
    # 通过Tag快速查询数据
    if search_type == "tag_search":
        # 获取第一页数据信息
        url_ = Url + "?article_tags__tag_name={}".format(search_data)
        # 计算获取数据的最大页码数
        count = int(GetData(url_)["count"])
        # 每页显示10条数据计算最大页码数，这里限制最多显示5页
        max_page = 5 if int(count / 10) > 5 else int(count / 10)
        # 如果当前页超出最大页 则显示最后一页内容
        currentPage = int(max_page if page > max_page else int(page))
        # 获取页面路径
        curr_url = request.get_full_path().split("/")[2].split("&page")[0]
        # 构建一级类别对应栏目的url
        url_ = Url + "?article_tags__tag_name={}&page={}".format(search_data, currentPage)
        # 解析API获取数据
        ArticleList = GetData(url_)

    # 各个栏目内容列表
    if search_type == "GetArticleItemInfo":
        # 获取一级大类、二级栏目、对应页码的API数据信息
        url_ = Url + "?category={}&item={}&page={}".format(category, item, page)
        # 计算获取数据的最大页码数
        count = int(GetData(url_)["count"])
        # 每页显示10条数据计算最大页码数，这里限制最多显示5页
        max_page = 5 if int(count / 10) > 5 else int(count / 10)
        # 解析API获取数据
        ArticleList = GetData(url_)

    elif search_type == "word_search":
        # 获取一级大类、二级栏目、对应页码的API数据信息
        url_ = Url + "?search={}&page={}".format(search_data, page)
        # 计算获取数据的最大页码数
        count = int(GetData(url_)["count"])
        # 每页显示10条数据计算最大页码数，这里限制最多显示5页
        max_page = 5 if int(count / 10) > 5 else int(count / 10)
        # 解析API获取数据
        ArticleList = GetData(url_)

    # 定义下一页和上一页url链接,如果没有数据用空字符串替换
    next_page_num, previous_pag_num = RePage(ArticleList["next"]), RePage(ArticleList["previous"])

    # 定义页码范围 page(当前页)
    if page < 5:
        page_max = 10 if max_page > 10 else max_page
        pageRange = range(1, page_max + 1)
    elif page > 5 and max_page < (page + 5):
        pageRange = range(page - 5, max_page + 1)
    elif page > 5 and max_page > (page + 5):
        pageRange = range(page - 5, page + 5)
    elif page > max_page:  # 超出最大页数
        page = max_page
        pageRange = range(page - 5, max_page + 1)

    return max_page, pageRange, ArticleList, next_page_num, previous_pag_num, page


# 用户购买订单提交功能
def UserOrderPost(Url, username, info_slug, consumption_integral):
    # 构建用户行为日志字典
    buy_data = {
        "username": username,
        "info_slug": info_slug,
        "consumption_integral": consumption_integral
    }
    result = requests.post(Url, headers=headers, data=json.dumps(buy_data))


# 更改用户积分（重置）
def UserProfileResetIntegralPut(Url, username, password, integral):
    # 构建用户修改积分字典
    reset_user_integral = {
        'username': username,
        'password': password,
        'integral': integral,
    }
    # 向服务器更新密码
    url = Url + username + "/"
    result = requests.put(url, headers=headers, data=json.dumps(reset_user_integral))


# 获取用户身份信息
def GetUserInfo(Url, request, username=None):
    # 如果未传入username则获取session中的username
    if not username:
        try:
            username = request.session["username"]
        except:
            username = "Tourist"
        UserInfo = None if username == 'Tourist' else GetData(urljoin(Url, username))
        return UserInfo
    # 传入参数username则执行
    else:
        username = username
        UserInfo = GetData(urljoin(Url, username))
        try:
            if UserInfo["username"]:
                return UserInfo
        except KeyError:
            return None


# 订阅邮件功能
def UserSubscriptionPost(Url, email):
    # 构建订阅数据字典
    data = {
        "email": email,
    }
    requests.post(Url, headers=headers, data=json.dumps(data))
    return "感谢您的订阅！"


# 用户留言
def MyHomeMessagePost(Url, name, email, subject, message):
    user_data = {
        "name": name,
        "email": email,
        "subject": subject,
        "content": message
    }
    # 向服务器注册用户
    a = requests.post(Url, headers=headers, data=json.dumps(user_data))


# IP记录信息
def VisitIpPost(Url, request, visit_part):
    # 记录访问ip和每个ip的次数,和访问的部分
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        visit_ip = request.META['HTTP_X_FORWARDED_FOR']
        visit_ip = visit_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        visit_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
    # 构建IP访问字典
    ip_data = {
        "visit_ip": visit_ip,
        "visit_part": visit_part
    }
    requests.post(Url, headers=headers, data=ip_data)
