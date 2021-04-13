# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 下午3:28
# @Author  : wth

# 单例装饰器
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton
