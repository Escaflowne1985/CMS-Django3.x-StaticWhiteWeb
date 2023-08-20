# coding:utf-8
__author__ = 'Mr数据杨'
__explain__ = '用户功能视图,部署统一修改BaseUrl' \
              '设置使用的API的Url和使用的HTML模板方便统一调用更改' \
              '1.UserRegisterView 用户注册' \
              '2.UserLoginView 用户登陆' \
              '3.UserLogoutView 用户登出' \
              '4.UserTokenInfoView 用户登陆API跳过CSRF验证' \
              '5.UserForgotPasswordView 用户忘密码通过邮箱获取邮件' \
              '6.UserInformationVerificationView 用户通过邮件的类型和验证码' \
              '7.UserResetPassWordView 用户通过邮件重置密码' \
              '8.AddFavView 用户收藏' \
              '9.AddShareView 用户分享' \
              '10.UserArticleListView 用户文章记录' \
              '11.UserBuyArticleView 用户购买内容' \
              '12.AdminUserCenterView 用户中心' \
              '13.AdminUserArticleDataView 用户后台数据展示'

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
# 加载邮件实用程序
from apps.utils.EmailTools import *
from apps.utils.TimeTools import *
from apps.utils.RequestTools import *
from apps.utils.Forms import *
from apps.utils.Msgs import *
# 加载settings中设置的API网址和端口号
from NewsWeb3.settings import ApiBaseUrl

# 设置API的Url
UserTokenLoginUrl = ApiBaseUrl + '/UserSettings/token_login/'  # 用户token生成API
UserProfileUrl = ApiBaseUrl + '/UserSettings/UserProfile/'  # 用户列表Url
UserProfileUpdateUrl = ApiBaseUrl + '/UserSettings/UserProfileUpdate/'  # 用户数据更新Url
UserSubscriptionUrl = ApiBaseUrl + '/UserSettings/UserSubscription/'  # 用户订阅Url
UserRegisterUrl = ApiBaseUrl + '/UserSettings/UserRegister/'  # 用户注册url
UserEmailVerifyRecordUrl = ApiBaseUrl + '/UserSettings/UserEmailVerifyRecord/'  # 用户邮件Url
UserFavUrl = ApiBaseUrl + '/UserSettings/UserFav/'  # 用户收藏Url
UserReadUrl = ApiBaseUrl + '/UserSettings/UserRead/'  # 用户浏览Url
UserShareUrl = ApiBaseUrl + '/UserSettings/UserShare/'  # 用户分享Url
UserOrderUrl = ApiBaseUrl + '/UserSettings/UserOrder/'
UserServerLogUrl = ApiBaseUrl + '/UserSettings/UserServerLog/'  # 用户列表用户操作日志Url
ArticleInfoUrl = ApiBaseUrl + '/ArticleSettings/ArticleInfo/'  # 内容基础信息Url

# 设置Html信息
UserLoginHtml = "users/UserLogin.html"  # 用户登陆页面
UserRegisterHtml = "users/UserRegister.html"  # 用户注册页面
UserForgotPasswordHtml = "users/UserForgotPassword.html"  # 用户找回密码页面
UserResetPasswordHtml = "users/UserResetPassword.html"  # 用户重置密码页面
UserArticlesHtml = 'users/UserArticles.html'  # 用户浏览、收藏、转载页面
UserUnLoginHtml = 'users/UserUnLogin.html'
UserCenterHtml = 'admin/UserCenter.html'
UserArticleDataHtml = 'admin/UserArticleList.html'


# 用户注册功能
class UserRegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        # CBV方式get注册页面
        return render(request, UserRegisterHtml, {"register_form": register_form})

    def post(self, request):
        # 实例化Form表单
        register_form = RegisterForm(request.POST)
        # 判断注册信息的Form表单是否合法
        if register_form.is_valid():
            username = request.POST.get("username")  # username数据
            email = request.POST.get("email")  # email数据
            password = request.POST.get("password")  # password数据
            mobile = request.POST.get("mobile")  # mobile数据

            # 用户数据查重部分
            if GetData(UserProfileUrl + '?username=' + username):
                # 用户查重
                return render(request, UserRegisterHtml, {"register_form": register_form, "msg": MSG_ExistedUser})
            elif GetData(UserProfileUrl + '?email=' + email):
                # 邮箱查重
                return render(request, UserRegisterHtml, {"register_form": register_form, "msg": MSG_ExistedEmail})
            elif GetData(UserProfileUrl + '?mobile=' + mobile):
                # 电话查重
                return render(request, UserRegisterHtml, {"register_form": register_form, "msg": MSG_ExistedTel})

            # post注册请求
            RegisterUserProfile(UserRegisterUrl, username, email, mobile, password)
            # post用户日志
            UserServerLogPost(
                UserServerLogUrl, username, MSG_UserActionRegistered, MSG_SuccessRegistered, "1", ""
            )
            # 发送注册激活邮件
            SendEmail(UserEmailVerifyRecordUrl, email, "register")
            # 跳转到登录页面
            return HttpResponseRedirect(reverse("UserLogin"))
        else:
            # post用户日志
            UserServerLogPost(
                UserServerLogUrl, "", MSG_UserActionRegistered, MSG_FailureRegistered, "0", ""
            )
            # 跳转填写Form错误提示
            return render(request, UserLoginHtml, {"register_form": register_form})


# 用户登陆功能
class UserLoginView(View):
    def get(self, request):
        login_form = LoginForm()
        # CBV方式get登陆页面
        return render(request, UserLoginHtml, {"login_form": login_form})

    def post(self, request):
        # 实例化Form表单
        login_form = LoginForm(request.POST)
        # 判断登陆信息的Form表单是否合法
        if login_form.is_valid():
            username = request.POST.get("username")  # username数据
            password = request.POST.get("password")  # password数据
            # 通过API获取登陆用户的数据
            UserInfo = GetUserInfo(UserProfileUrl, request, username)
            # 判断用户是否存在
            if not UserInfo:
                # 用户不存在错误跳转
                return render(request, UserLoginHtml, {"msg": MSG_ErrorUserInfo})
            else:
                # 验证用户密码
                CheckPassword = check_password(password, UserInfo["password"])
                # 用户密码验证成功
                if CheckPassword:
                    # post用户日志
                    UserServerLogPost(
                        UserServerLogUrl, username, MSG_UserActionLogin, MSG_SuccessCheckPassword, "1", ""
                    )
                    # 验证用户激活状态
                    if UserInfo["is_active"]:
                        # 在session中添加登陆状态、用户名、jtw_token
                        request.session['is_login'] = "True"
                        request.session['username'] = username
                        request.session['jwt_token'] = UserJWTTokenPost(UserTokenLoginUrl, username, password)
                        # post用户日志
                        UserServerLogPost(
                            UserServerLogUrl, username, MSG_UserActionLogin, MSG_SuccessLogin, "1",
                            request.session['jwt_token']
                        )
                        # 跳转到主页
                        return redirect('HomePage')
                    else:
                        # post用户日志
                        UserServerLogPost(
                            UserServerLogUrl, username, MSG_UserActionLogin, MSG_FailureLogin, "0", ""
                        )
                        # 跳转账号未通过邮箱激活提示
                        return render(request, UserLoginHtml, {"msg": MSG_NotActiveUser})
                # 用户密码验证失败
                else:
                    # post用户日志
                    UserServerLogPost(
                        UserServerLogUrl, username, MSG_UserActionLogin, MSG_FailureCheckPassword, "0", ""
                    )
                    # 跳转Form错误提示
                    return render(request, UserLoginHtml, {"msg": MSG_ErrorUserInfo})
        else:
            # post用户日志
            UserServerLogPost(UserServerLogUrl, "", MSG_UserActionLogin, MSG_UserActionErrorFormInfo, "0", "")
            # 跳转填写Form错误提示
            return render(request, UserLoginHtml, {"login_form": login_form})


# 用户登出功能
class UserLogoutView(View):
    def get(self, request):
        username = request.session["username"]
        # 在session中添加登出状态
        request.session['is_login'] = "False"
        request.session['jwt_token'] = ""
        request.session['username'] = "Tourist"

        # post用户日志
        UserServerLogPost(
            UserServerLogUrl, username, MSG_UserActionLogout, MSG_SuccessLogout, "1", ""
        )

        return redirect('HomePage')


# 用户登陆API跳过CSRF验证View 通过JS生成username和jwt_token保存到浏览器中
class UserTokenInfoView(View):
    def post(self, request):
        username = request.POST.get("username")  # username数据
        password = request.POST.get("password")  # password数据
        # 访问API返回用户名和token信息
        return_data = UserInfoTokenPost(UserTokenLoginUrl, username, password)
        # post用户日志
        UserServerLogPost(
            UserServerLogUrl, username, MSG_UserActionLogin, MSG_SuccessToken, "1", return_data["jwt_token"]
        )
        # 通过JS访问将数据返回给前端
        return HttpResponse(str(return_data))

    # 这里要跳过CSRF验证
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(UserTokenInfoView, self).dispatch(*args, **kwargs)


# 用户忘密码通过邮箱获取邮件功能
class UserForgotPasswordView(View):
    def get(self, request):
        # CBV方式get忘记密码页面
        return render(request, UserForgotPasswordHtml)

    def post(self, request):
        # 实例化Form表单
        forgot_form = ForgotForm(request.POST)
        email = request.POST.get("email")  # email数据
        # 验证用户邮箱是否存在
        if not GetData(UserProfileUrl + '?email=' + email):
            # post用户日志
            UserServerLogPost(
                UserServerLogUrl, email, MSG_UserActionResetPassword, MSG_FailureResetPasswordEmail, "0", ""
            )
            # 跳转填写Form错误提示
            return render(request, UserForgotPasswordHtml,
                          {"forgot_form": forgot_form, "msg": MSG_FailureResetPasswordEmail})
        # 邮箱验证正确
        if forgot_form.is_valid():
            # post用户日志
            UserServerLogPost(
                UserServerLogUrl, email, MSG_UserActionResetPassword, MSG_SuccessResetPasswordEmail, "1", ""
            )
            # 发送密码找回邮件到用户邮箱
            SendEmail(UserEmailVerifyRecordUrl, email, "forgot")
            # 跳转到主页
            return redirect(reverse("UserLogin"))
        # 跳转填写Form错误提示
        return render(request, UserForgotPasswordHtml, {"forgot_form": forgot_form})


# 用户通过邮件的类型和验证码功能
class UserInformationVerificationView(View):
    # CBV方式get注册页面
    def get(self, request):
        OperationType = request.GET.get("OperationType")
        Code = request.GET.get("Code")
        Email = request.GET.get("Email")
        # 验证系统邮件的时效性和有效性，构建数据字典 {'status':xx,'data':xx,'type':xx,'code':xx} 的格式
        EmailVerifyRecord = EmailVerifyRecordData(OperationType, Code, Email)

        # 验证返回验证数据字典的status
        if EmailVerifyRecord["status"] is True:
            type_ = EmailVerifyRecord["type"]
            email_ = EmailVerifyRecord["email"]
            # 注册业务内容操作
            if type_ == 'register':
                # 通过注册邮箱获取用户信息
                UserInfo = GetData(UserProfileUrl + "?email={}".format(email_))[0]
                # 通过注册信息获取post修改用户信息的条件
                username = UserInfo["username"]  # 用户名
                password = UserInfo["password"]  # 用户密码
                is_active = UserInfo["is_active"]  # 用户激活状态
                # 用户已激活
                if is_active is True:
                    return HttpResponse("账号已激活，请勿重复提交！！！")  # 这里未来制作一个可视化页面
                # 用户未激活
                else:
                    # put用户is_active进行激活
                    UserProfileActivePut(UserProfileUpdateUrl, username, password)
                    # post用户日志
                    UserServerLogPost(
                        UserServerLogUrl, username, MSG_UserActionLogin, MSG_SuccessActive, "1", ""
                    )
                    return HttpResponse("恭喜激活账号")  # 这里未来制作一个可视化页面

            # 根据业务类型进行不同的页面跳转以及操作，忘记密码重置密码部分
            if type_ == 'forgot':
                return HttpResponseRedirect(reverse('UserResetPassWord',
                                                    kwargs={
                                                        'OperationType': EmailVerifyRecord["type"],
                                                        'Code': EmailVerifyRecord["code"],
                                                        'Email': EmailVerifyRecord["email"],
                                                    }
                                                    ))
        # 邮件验证失效
        if EmailVerifyRecordResultDict["status"] is False:
            return HttpResponse("激活码邮件已过期或者验证码不正确，请重新注册激活！！！")  # 这里未来制作一个可视化页面


# 用户通过邮件重置密码功能
class UserResetPasswordView(View):
    def get(self, request, OperationType, Code, Email):
        # 邮件验证码的验证
        EmailVerifyRecord = EmailVerifyRecordData(OperationType, Code, Email)
        # 获取重置密码的链接
        if EmailVerifyRecord['status'] is True:
            return render(request, UserResetPasswordHtml)
        else:
            return HttpResponse("激活码邮件已过期或者验证码不正确，请重新注册激活！！！")  # 这里未来制作一个可视化页面

    def post(self, request, OperationType, Code, Email):
        # 信息提交验证
        EmailVerifyRecord = EmailVerifyRecordData(OperationType, Code, Email)
        # 实例化Form表单
        reset_form = ResetForm(request.POST)
        # 验证通过
        if EmailVerifyRecord['status'] is True:
            # 判断重置密码的Form表单是否合法
            if reset_form.is_valid():
                username = request.POST.get("username")
                password = request.POST.get("password")
                # put用户password重置密码
                UserProfileResetPasswordPut(UserProfileUpdateUrl, username, password)
                # post用户日志
                UserServerLogPost(
                    UserServerLogUrl, username, MSG_UserActionResetPassword, MSG_SuccessResetPassword, "1", ""
                )
                return HttpResponse("密码重置成功！！")  # 这里未来制作一个可视化页面
        # 邮件验证失效
        else:
            return HttpResponse("激活码邮件已过期或者验证码不正确！！！")  # 这里未来制作一个可视化页面


# 用户阅读记录
class UserArticleReadView(View):
    def get(self, request):
        UserInfo = GetUserInfo(UserProfileUrl, request)  # 通过Session获取用户登陆信息
        # 这里判断用户是否登陆，未登陆提示500
        if UserInfo is None:
            return render(request, UserUnLoginHtml, status=500)
        else:
            username = request.session["username"]
            article_type = request.GET.get("article_type")
            url_type_dict = {
                "All": UserReadUrl,  # 全部数据
                "Read": UserReadUrl,  # 用户浏览数据
                "Fav": UserFavUrl,  # 用户收藏数据
                "Share": UserShareUrl  # 用户分享数据
            }
            name_type_dict = {
                "All": "全部数据",  # 全部数据
                "Read": "浏览数据",  # 用户浏览数据
                "Fav": "收藏数据",  # 用户收藏数据
                "Share": "分享数据"  # 用户分享数据
            }
            # 全部数据根据ID排序展示
            if article_type == "All":
                records_read = GetData(url_type_dict["Read"] + "?user__username={}".format(username))
                records_fav = GetData(url_type_dict["Fav"] + "?user__username={}".format(username))
                records_share = GetData(url_type_dict["Share"] + "?user__username={}".format(username))
                records = records_read + records_fav + records_share
                # list根据id序号排序
                records = sorted(records, key=lambda i: i['id'], reverse=True)
                # 将列表的结果拼接成字符串符合API接口规范
                result_list = ",".join(list(set([i["article_slug"] for i in records])))
                # 根据拼接的字符串访问接口获取用户的对应文章Info数据
                user_center_article_info = \
                    GetData(ArticleInfoUrl + "?user_center_article_info=" + result_list)
                user_center_article_info_number, user_center_article_info_name = \
                    len(user_center_article_info["results"]), name_type_dict["All"]
                current_page, data_list, curr_url = TurnPage(request, user_center_article_info)
                return render(request, UserArticlesHtml, locals())
            # 根据选择的类别进行展示
            else:
                # 根据用户名和文章slug查询是否该用户收藏该slug文章
                records = GetData(url_type_dict[article_type] + "?user__username={}".format(username))
                # list根据id序号排序
                records = sorted(records, key=lambda i: i['id'], reverse=True)
                # 将列表的结果拼接成字符串符合API接口规范
                result_list = ",".join(list(set([i["article_slug"] for i in records])))
                # 根据拼接的字符串访问接口获取用户的对应文章Info数据
                user_center_article_info = GetData(ArticleInfoUrl + "?user_center_article_info=" + result_list)
                # 返回结果的数据数量
                user_center_article_info_number = len(user_center_article_info["results"])
                # 搜索类型名称
                user_center_article_info_name = name_type_dict[article_type]
                current_page, data_list, curr_url = TurnPage(request, user_center_article_info)
                return render(request, UserArticlesHtml, locals())


# 用户收藏行为
class UserArticleFavView(View):
    def get(self, request, info_slug):
        UserInfo = GetUserInfo(UserProfileUrl, request)  # 通过Session获取用户登陆信息
        # 这里判断用户是否登陆，未登陆提示500
        if UserInfo is None:
            return render(request, UserUnLoginHtml, status=500)
        else:
            username = request.session["username"]
            # 根据用户名和文章slug查询是否该用户收藏该slug文章
            exist_records = GetData(
                UserFavUrl + "?username={}&info_slug={}".format(username, info_slug)
            )
            if exist_records:
                # 记录已经存在，表示用户想要取消收藏
                fav_id = exist_records[0]["id"]  # 解析数据获取收藏内容的id
                requests.delete(UserFavUrl + '{}/'.format(fav_id))
                return HttpResponse('{"status":"success", "msg":"取消收藏成功"}', content_type='application/json')
            else:
                # 记录不存在则通过API写入收藏
                UserFavShareReadPost(UserFavUrl, username, info_slug)
                return HttpResponse('{"status":"success", "msg":"添加收藏成功"}', content_type='application/json')


# 用户分享行为 (这个功能前端暂时不知道怎么写，暂时先pass)
class UserArticleShareView(View):
    def get(self, request, info_slug):
        UserInfo = GetUserInfo(UserProfileUrl, request)  # 通过Session获取用户登陆信息
        # 这里判断用户是否登陆，未登陆提示500
        if UserInfo is None:
            return render(request, UserUnLoginHtml, status=500)
        else:
            username = request.session["username"]
            # 根据用户名和文章slug查询是否该用户收藏该slug文章
            exist_records = GetData(
                UserShareUrl + "?username={}&info_slug={}".format(username, info_slug))

            if exist_records:
                # 记录已经存在， 表示用户想要取消收藏
                return HttpResponse('{"status":"success", "msg":"已分享过了"}', content_type='application/json')
            else:
                # 记录不存在则通过API写入收藏
                UserFavShareReadPost(UserShareUrl, username, info_slug)
                return HttpResponse('{"status":"success", "msg":"分享成功"}', content_type='application/json')


# 用户购买内容
class UserBuyArticleView(View):
    def get(self, request, info_slug):
        UserInfo = GetUserInfo(UserProfileUrl, request)  # 通过Session获取用户登陆信息
        # 这里判断用户是否登陆，未登陆提示500
        if UserInfo is None:
            return render(request, UserUnLoginHtml, status=500)
        else:
            username = request.session["username"]
            # 通过API获取登陆用户的数据
            UserInfo = GetData(urljoin(UserProfileUrl, username))
            user_integral = UserInfo["integral"]
            user_password = UserInfo["password"]
            ArticleInfo = GetData(urljoin(ArticleInfoUrl, info_slug))
            article_integral = ArticleInfo["integral_num"]
            # 判断是否已经购买，避免重复消耗积分购买
            # 根据用户名和文章slug查询是否该用户购买过slug文章
            exist_records = GetData(
                UserOrderUrl + "?username={}&info_slug={}".format(username, info_slug))
            if exist_records:
                # 这里未来制作一个可视化页面
                return HttpResponse('{"status":"success", "msg":"已购买请勿重复购买"}',
                                    content_type='application/json')
            else:
                # 判断积分余额
                if user_integral >= article_integral:
                    result_integral = user_integral - article_integral
                    # post积分请求更新减去的对应积分
                    UserProfileResetIntegralPut(UserProfileUpdateUrl, username, user_password, result_integral)
                    # post订单请求
                    UserOrderPost(UserOrderUrl, username, info_slug, article_integral)
                    # post用户日志
                    UserServerLogPost(
                        UserServerLogUrl, username, MSG_UserActionExchangeArticle, MSG_SuccessExchangeArticle, "1",
                        info_slug
                    )
                    return HttpResponse('{"status":"success", "msg":"已购买成功"}',
                                        content_type='application/json')  # 这里未来制作一个可视化页面
                else:
                    UserServerLogPost(
                        UserServerLogUrl, username, MSG_UserActionExchangeArticle, MSG_FailureExchangeArticle, "0",
                        info_slug
                    )
                    return HttpResponse('{"status":"success", "msg":"购买失败积分不足"}',
                                        content_type='application/json')  # 这里未来制作一个可视化页面


############# 用户Admin #############
class AdminUserCenterView(View):
    def get(self, request):
        UserInfo = GetUserInfo(UserProfileUrl, request)  # 通过Session获取用户登陆信息
        # 这里判断用户是否登陆，未登陆提示500
        if UserInfo is None:
            return render(request, UserUnLoginHtml, status=500)
        else:
            username = request.session["username"]
            UserInfo = GetData(urljoin(UserProfileUrl, username))
            return render(request, UserCenterHtml, {"UserInfo": UserInfo})


class AdminUserArticleDataView(View):
    def get(self, request):
        UserInfo = GetUserInfo(UserProfileUrl, request)  # 通过Session获取用户登陆信息
        # 这里判断用户是否登陆，未登陆提示500
        if UserInfo is None:
            return render(request, UserUnLoginHtml, status=500)
        else:
            username = request.session["username"]
            type_ = request.GET.get('type')  # 获取用户中心的文章类型
            type_dict = {
                "buy": UserOrderUrl,
                "read": UserReadUrl,
                "fav": UserFavUrl,
            }
            data_url = type_dict[type_]
            records = GetData(data_url + "?user__username={}".format(username))
            article_slug_list = list(set([i["article_slug"] for i in records]))  # 对获取的文章slug进行去重

            ArticleInfoList = []
            for slug in article_slug_list:
                ArticleInfo = GetData(urljoin(ArticleInfoUrl, slug))
                ArticleInfoList.append(ArticleInfo)
            return render(request, UserArticleDataHtml, {"ArticleInfoList": ArticleInfoList})
