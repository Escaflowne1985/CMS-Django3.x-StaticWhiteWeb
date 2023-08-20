# -*- coding: utf-8 -*-
__author__ = 'Mr.数据杨'
__explain__ = '用于验证用户在Web前端填写的数据是否有效而设置，减轻服务器压力用' \
              '1.登陆验证' \
              '2.注册验证' \
              '3.密码找回验证' \
              '4.密码重置验证' \
              '' \
              '表单验证主要参数解释' \
              '1.required=True 填写内容不能为空' \
              '2.min_length=5 最小长度是5' \
              '3.error_messages={"invalid": "验证码错误"} 验证码返回错误提示'

from captcha.fields import CaptchaField
from django import forms


# 登陆验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


# 注册验证
class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


# 忘记密码验证
class ForgotForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


# 重置密码验证
class ResetForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
