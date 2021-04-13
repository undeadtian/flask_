# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 下午4:41
# @Author  : wth

# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 下午3:33
# @Author  : wth

from proto import filter_conf_pb2
from proto import sensor_source_pb2
from google.protobuf import text_format
import time
from common.Log import Logger

logger = Logger('FilterConfig').getlog()


class FilterConfig(object):
    def __init__(self, file='/home/wth/fabu/calibration-master/conf/filter.conf'):
        self.conf_file = file
        self.config = self._get_conf()

    def _save_conf(self):
        f = open(self.conf_file, "w+")
        f.write(text_format.MessageToString(self.config))
        f.close()

    # 只对filter的中间结果备份
    def _bk_conf(self, mode, device_id):
        if mode != 'filter':
            return
        rq = time.strftime("%Y%m%d%H%M", time.localtime())
        f = open(self.conf_file.replace('.', f'{rq}.'), "w")
        f.write(text_format.MessageToString(self.config))
        f.close()

    def _get_conf(self):
        with open(self.conf_file, 'r+') as f:
            message = f.read()
        return text_format.Parse(message, filter_conf_pb2.FilterConf())

    def mod_filter_config(self, post_data):
        tmp_config = self.config
        tmp_config.is_use_voxel_grid = post_data.get('is_use_voxel_grid')
        tmp_config.lx = float(post_data.get('lx'))
        tmp_config.ly = float(post_data.get('ly'))
        tmp_config.lz = float(post_data.get('lz'))
        tmp_config.is_use_statistical_outlier_removal = post_data.get('is_use_statistical_outlier_removal')
        tmp_config.mean_k = float(post_data.get('mean_k'))
        tmp_config.stddevmulthresh = float(post_data.get('stddevmulthresh'))


# def ModConf():

if __name__ == '__main__':
    # getConf()
    A = FilterConfig('/home/wth/fabu/calibration-master_t/conf/filter.conf')
    A.config.lx = 0.5
    A._save_conf()
