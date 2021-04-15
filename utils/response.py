# -*- coding: utf-8 -*-
# @DateTime : 2021/4/14-下午1:55
# @Author   : byron

from flask import jsonify


class HttpCode(object):
    success = 0
    params_error = 1
    params_format_error = 2
    param_not_defined = 3
    # 服务器端解析数据失败，数据库获取数据失败
    get_data_failed = 4
    # 服务器端运行脚本错误，其他问题：
    server_error = 5


def resp_result(code, msg, data):
    return jsonify(code=code, msg=msg, data=data or {})


def success(msg, data=None):
    return resp_result(code=HttpCode.success, msg=msg, data=data)


def error(code, msg, data=None):
    return resp_result(code=code, msg=msg, data=data)
