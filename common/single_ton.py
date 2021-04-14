# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 下午3:28
# @Author  : wth
from functools import wraps


# 单例装饰器
def singleton(cls):
    _instances = {}

    @wraps(cls)
    def _singleton(*args, **kargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kargs)
        return _instances[cls]

    return _singleton
