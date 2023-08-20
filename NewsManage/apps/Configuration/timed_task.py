# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '全局控制定时任务'

# 每日定时备份blog的内容发送文件到 QQ邮箱
# 此方式仅限Linux执行

from apps.Article.models import *
from apps.StatisticalData.models import *
from apps.User.models import *
import pandas as pd
from NewsManage.settings import *
from django.core.mail import EmailMessage
import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from email.header import make_header
from email.mime.text import MIMEText  # html格式和文本格式邮件
from email.mime.image import MIMEImage  # 带图片格式邮件
import os

EMAIL_HOST_USER = "33034782@qq.com"


# 备份文件
def backups_blog():
    # 读取文章的基本内信息
    df = pd.DataFrame(list(ArticleInfo.objects.all().values()))
    # 读取item的外键关联数据
    df_dict = pd.DataFrame(list(ArticleItem.objects.all().values()))
    df_dict = dict(zip(df_dict['id'], df_dict['item_name']))
    df["article_item_id"] = df["article_item_id"].map(df_dict)
    df.to_excel(BASE_DIR + "/backups_data/blog_info.xlsx")

    # 当天日期
    today = datetime.date.today()

    subject = str(today) + ' 文章和视频内容备份'
    text_content = str(today) + "备份信息"
    html_content = '<h3><span style="color: red; font-size: 25px;">{}</span>备份文件</h3>'.format(str(today))
    from_email = EMAIL_HOST_USER
    receive_email_addr = [EMAIL_HOST_USER]
    msg = EmailMultiAlternatives(subject, text_content, from_email, receive_email_addr)
    msg.attach_alternative(html_content, "text/html")

    # 添加附件
    file_path = os.path.join(BASE_DIR + "/backups_data/blog_info.xlsx")
    text = open(file_path, 'rb').read()
    file_name = os.path.basename(file_path)
    b = make_header([(file_name, 'utf-8')]).encode('utf-8')
    msg.attach(b, text)

    file_path = os.path.join(BASE_DIR + "/backups_data/blog_video_info.xlsx")
    text = open(file_path, 'rb').read()
    file_name = os.path.basename(file_path)
    b = make_header([(file_name, 'utf-8')]).encode('utf-8')
    msg.attach(b, text)
    msg.send()
