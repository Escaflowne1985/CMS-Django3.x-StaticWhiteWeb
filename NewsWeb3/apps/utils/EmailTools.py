# -*- coding: utf-8 -*-
__author__ = 'Mr.数据杨'
__date__ = '发送邮件实用程序，部署需要重新定义BaseUrl' \
           '1.RandomsStr 随机生成邮件验证码的随机字符串' \
           '2.SendEmail 发送邮件功能，定义注册用户、密码找回' \
           '3.EmailVerifyRecordData 验证邮件操作类型是否可以操作，其中有时效验证环节'

import requests
import json
from random import Random
from django.core.mail import EmailMessage  # Django邮件模块
from NewsWeb3.settings import EMAIL_FROM  # setting中发送邮件的配置
from django.template import loader  # 发送html格式的邮件
from apps.utils.RequestTools import *
from apps.utils.TimeTools import *
# 加载settings中设置的API网址和端口号
from NewsWeb3.settings import ApiBaseUrl

WebBaseUrl = "http://127.0.0.1/"
UserInformationVerificationUrl = ApiBaseUrl + '/UserSettings/UserEmailVerifyRecord/'


# 随机生成邮件验证码的随机字符串
def RandomsStr(random_length):
    Str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'  # 设置可选字符
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        Str += chars[random.randint(0, length)]
    return Str


# 发送邮件设置
def SendEmail(UserEmailVerifyRecordUrl, email, send_type):
    # 生成20位的验证码
    code = RandomsStr(16)
    # 设置邮箱验证内容的字典
    CodeDict = {
        'register': {
            "EmailTitle": "欢迎注册Mr.数据杨的家庭健康中医数字服务平台，请点击注册激活链接",
            "EmailHtml": "users/EmailRegister.html",
            "EmailUrl": WebBaseUrl +
                        'UserInformationVerification/?Email={}&OperationType={}&Code={}'.format(email, send_type, code)
        },
        'forgot': {
            "EmailTitle": "Mr.数据杨的家庭健康中医数字服务平台，请点击找回密码链接",
            "EmailHtml": "users/EmailForgot.html",
            "EmailUrl": WebBaseUrl +
                        'UserInformationVerification/?Email={}&OperationType={}&Code={}'.format(email, send_type, code)
        },
    }
    # 根据send_type确定邮件的内容
    EmailTitle = CodeDict[send_type]["EmailTitle"]
    EmailHtml = CodeDict[send_type]["EmailHtml"]
    EmailUrl = CodeDict[send_type]["EmailUrl"]

    # 构建邮件类型字典
    email_verifyRecord_data = {
        'code': code,
        'email': email,
        'send_type': send_type,
    }
    # 设置注册post请求headers
    headers = {
        'content-type': 'application/json'
    }
    # 通过post将code写入API
    requests.post(UserEmailVerifyRecordUrl, headers=headers, data=json.dumps(email_verifyRecord_data))
    # 发送邮件
    EmailBody = loader.render_to_string(
        EmailHtml,  # 需要渲染的html模板
        {"active_code": code,
         "email_url": EmailUrl}  # 参数
    )
    msg = EmailMessage(EmailTitle, EmailBody, EMAIL_FROM, [email])
    msg.content_subtype = "html"
    msg.send()


# 验证邮件操作类型是否可以操作，其中有时效验证环节
def EmailVerifyRecordData_old(request):
    # 获取邮件的type和code
    _type = request.GET.get('OperationType')
    _code = request.GET.get('Code')
    _email = request.GET.get('Email')
    # 验证code有效性
    url_ = UserInformationVerificationUrl + "?email={}&code={}&type={}".format(_email, _code, _type)
    EmailVerifyRecord = GetData(url_)
    # 验证邮件的时效性 1000秒内有效
    EmailVerifyRecordResult = EmailCheckTime(EmailVerifyRecord)

    if EmailVerifyRecordResult is True:
        EmailVerifyRecordResultDict = {
            "status": True,
            "data": _email,
            "type": _type,
            "code": _code
        }
        return EmailVerifyRecordResultDict
    if EmailVerifyRecordResult is False:
        EmailVerifyRecordResultDict = {
            "status": False,
            "data": "激活码邮件已过期或者验证码不正确，请重新注册激活！！！",
            "type": _type,
            "code": _code
        }
        return EmailVerifyRecordResultDict


# 验证邮件操作类型是否可以操作，其中有时效验证环节
def EmailVerifyRecordData(OperationType, Code, Email):
    # 生成验证email、code、type的url链接
    url_ = UserInformationVerificationUrl + "?email={}&code={}&type={}".format(Email, Code, OperationType)
    # 验证code有效性
    EmailVerifyRecord = GetData(url_)
    # 验证邮件的时效性 1000秒内有效
    EmailVerifyRecordResult = EmailCheckTime(EmailVerifyRecord)

    if EmailVerifyRecordResult is True:
        EmailVerifyRecordResultDict = {
            "status": True,
            "email": Email,
            "type": OperationType,
            "code": Code
        }
        return EmailVerifyRecordResultDict
    if EmailVerifyRecordResult is False:
        EmailVerifyRecordResultDict = {
            "status": False,
            "msg": "激活码邮件已过期或者验证码不正确，请重新注册激活！！！",
            "type": OperationType,
            "code": Code
        }
        return EmailVerifyRecordResultDict
