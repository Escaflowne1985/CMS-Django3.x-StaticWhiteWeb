# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = '时间相关处理程序' \
              '1.CheckTime 用于验证获取时间是否在有效范围内'

import time


# 用于验证获取时间是否在有效范围内
def EmailCheckTime(EmailVerifyRecord):
    TimeDifference = 1000  # 设置时间差 单位秒
    # 验证是否EmailVerifyRecord存在可以提取send_time
    try:
        send_time = EmailVerifyRecord[-1]["send_time"].split(".")[0]
        send_time = time.strptime(send_time, '%Y-%m-%dT%H:%M:%S')  # 转换日期格式
        stamp = int(time.mktime(send_time))  # 转换成时间戳
        stamp_now = int(time.time())
        stamp_t = stamp_now - stamp
        if stamp_t >= TimeDifference:
            return False
        else:
            return True
    except:
        return False
