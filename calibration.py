# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 上午9:56
# @Author  : wth

from config.constant import const
from config.env_config import Config
from utils.drsu_cali_control import DRSUCaliControl
from utils.drsu_info import DRSUInfo
from utils.response import HttpCode, error, success
from utils.cali_env import DRSUEnv
from common.Log import Logger


logger = Logger('Calibration').getlog()


def check_int(obj):
    if isinstance(obj,int):
        return obj
    elif isinstance(obj, str):
        try:
            obj = int(obj)
            return obj
        except ValueError:
            logger.error('输入参数错误')
            return None
    else:
        logger.error('输入参数错误')


class Calibration(object):
    def __init__(self, project=None, drsu_id=None, config_file=None):
        self._project = project
        self._drsu_id = drsu_id
        self._config = Config(config_file if config_file else 'env_config.ini')
        self._drsu = None
        self._drsu_info_all = DRSUInfo().info

    def get_drsu_info(self):
        return self._drsu_info_all

    def prepare_env(self):
        if not self._project or self._drsu_id:
            logger.error('未指定项目名称与drsuid')
            return False
        ret = DRSUEnv(self._project, self._drsu_id, )

    # 数据的准确性有调用者保证
    @property
    def drsu_id(self):
        return self._drsu_id

    @drsu_id.setter
    def drsu_id(self, drsu_id):
        self._drsu_id = drsu_id

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project):
        self._project = project





if __name__ == '__main__':
    a = Calibration()
    a.drsu_id = 11
    print(a.drsu_id)
