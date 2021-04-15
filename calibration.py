# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 上午9:56
# @Author  : wth
import os

from config.constant import const
from config.env_config import Config, EnvConfig
from utils.drsu_cali_control import DRSUCaliControl
from utils.drsu_info import DRSUInfo
from utils.response import HttpCode, error, success
from utils.cali_env import DRSUEnv
from utils.cali_config import CaliConfig
from common.Log import Logger
from utils.calibration_control import CalibrationControlSingleton

logger = Logger('Calibration').getlog()
env_config = EnvConfig()


def check_int(obj):
    if isinstance(obj, int):
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
    def __init__(self, project=None, drsu_id=None, camera_type=None):
        self._project = project
        self._drsu_id = drsu_id
        self._camera_type = camera_type
        self._drsu = None
        self._drsu_info_all = DRSUInfo().info
        self._cali_control = None
        self._cur_root_dir = None
        self._fix_cam_conf = None

    def get_drsu_info(self):
        return self._drsu_info_all

    def prepare_env(self, force=False):
        if not self._project or self._drsu_id:
            logger.error('未指定项目名称与drsuid')
            return False
        drsu_env = DRSUEnv(self._project, self._drsu_id, env_config.tar_path, env_config.root_path,
                           env_config.remote_host, env_config.remote_port, env_config.remote_path,
                           force, username=env_config.user_name, password=env_config.password)
        ret = drsu_env.prepare_for_cali_env()
        return ret

    def get_calibration_handle(self):
        if not self._cali_control:
            drsu_name = '_'.join([const.PROJECT_NAME[self.project], 'drsu_{}'.format(self.drsu_id)])
            root_dir = self.get_cur_root_dir()
            self._cali_control = CalibrationControlSingleton(drsu_name, env_config.cali_path,
                                                             env_config.local_host, env_config.local_port,
                                                             root_dir)
        return self._cali_control

    def merge(self):
        cali_handle = self.get_calibration_handle()
        ret = cali_handle.send_msg_wait(const.MODE_MERGE)
        return ret

    def filter(self):
        cali_handle = self.get_calibration_handle()
        ret = cali_handle.send_msg_wait(const.MODE_FILTER)
        return ret

    # 下发计算指令，目前只有计算指令有图片输出，所以在filter指令后需要跟计算指令才能看filter效果
    def calibrate(self):
        cali_handle = self.get_calibration_handle()
        ret = cali_handle.send_msg_wait(const.MODE_CALIBRETE)
        return ret

    def get_init_fix_cam_conf(self):
        if not self._fix_cam_conf:
            self._fix_cam_conf = CaliConfig(os.path.join(self._cur_root_dir,
                                                         'fixed_cam_calib_{}.conf'.format(self._camera_type)))
        return self._fix_cam_conf

    def get_cur_root_dir(self):
        if not self._cur_root_dir:
            self._cur_root_dir = os.path.join(env_config.cali_path, env_config.root_path,
                                              self._project, 'drsu_{}'.format(str(self.drsu_id).rjust(2, '0')))
        return self._cur_root_dir

    def re_init(self):
        self.get_cur_root_dir()
        self.get_init_fix_cam_conf()

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

    @property
    def camera_type(self):
        return self._camera_type

    @camera_type.setter
    def camera_type(self, camera_type):
        if not self._project or self._drsu_id:
            logger.error('指定相机类型前请先指定指定项目名称与drsuid')
            return
        self._camera_type = camera_type
        self.re_init()


if __name__ == '__main__':
    a = Calibration()
    a.drsu_id = 11
    print(a.drsu_id)
