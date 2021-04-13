# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 下午3:25
# @Author  : wth
import pandas as pd
from common.single_ton import singleton


@singleton
class ResultControl(object):
    def __init__(self, project_name, drsu_id):
        self._project = project_name
        self._drsu_id = drsu_id
