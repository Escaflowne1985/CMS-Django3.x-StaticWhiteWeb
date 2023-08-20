# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '实用应用程序配置'

from django.template import loader
from random import Random
from MyHome.settings import *
from django.core.mail import EmailMessage
import datetime
from apps.User.models import *


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
def SendEmail(username, email, send_type):
    # 生成20位的验证码
    code = RandomsStr(20)
    # 设置邮箱验证内容的字典
    CodeDict = {
        'register': {
            "EmailTitle": "欢迎注册Mr.数据杨的个人博客空间，请点击注册激活链接",
            "EmailHtml": "User/EmailRegister.html",
            "EmailUrl": WebBaseUrl + '/EmailVerifyRecord?Username={}&Type={}&Code={}'.format(username, send_type, code)
        },
        'forgot': {
            "EmailTitle": "欢迎Mr.数据杨的个人博客空间，请点击找回密码链接",
            "EmailHtml": "User/EmailForgot.html",
            "EmailUrl": WebBaseUrl + '/EmailVerifyRecord?Username={}&Type={}&Code={}'.format(username, send_type, code)
        },
    }
    # 根据send_type确定邮件的内容
    EmailTitle = CodeDict[send_type]["EmailTitle"]
    EmailHtml = CodeDict[send_type]["EmailHtml"]
    EmailUrl = CodeDict[send_type]["EmailUrl"]

    # 将邮件验证信息保存
    user_email_verify_record = UserEmailVerifyRecord()
    user_email_verify_record.username = username
    user_email_verify_record.send_type = send_type
    user_email_verify_record.email = email
    user_email_verify_record.code = code
    user_email_verify_record.save()

    # 发送邮件功能
    EmailBody = loader.render_to_string(
        EmailHtml,  # 需要渲染的html模板
        {"email_url": EmailUrl}  # 邮箱验证信息的url参数
    )
    msg = EmailMessage(EmailTitle, EmailBody, EMAIL_FROM, [email])
    msg.content_subtype = "html"
    msg.send()


# 用于验证获取时间是否在有效范围内
def CheckTime(record_time):
    start_time = record_time
    end_time = datetime.datetime.now()
    time_interval_seconds = (end_time - start_time).seconds
    if time_interval_seconds <= 2000:
        return True
    else:
        return False
