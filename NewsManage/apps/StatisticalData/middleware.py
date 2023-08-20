# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = '日志自定义中间件'

import logging
import json

class ApiLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.apiLogger = logging.getLogger('api')

    def __call__(self, request):
        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()
        body.update(dict(request.POST))
        response = self.get_response(request)
        if request.method != 'GET':
            self.apiLogger.info("{} {} {} {} {} {}".format(
                request.user, request.method, request.path, body,
                response.status_code, response.reason_phrase))
        return response
