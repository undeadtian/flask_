# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 上午10:20
# @Author  : wth

import os
import pandas as pd
from common.Log import Logger
from config.constant import const

logger = Logger('DRSUInfo').getlog()


class ProjectInfo(object):
    def __init__(self, proj_name, columns=None):
        self.proj_name = proj_name
        columns_default = ['序号', '类型', '点位名']
        self.columns = columns if columns else columns_default
        self.drsu_list = self._parse_proj_csv()

    def _parse_proj_csv(self, ):
        """
        Input: columns: 需要抽取的数据列名称列表
        Output: drsu_list:
        [{'序号': 1, '类型': '路灯', '点位名': 'DRSU1', ...},
         {'序号': 4, '类型': '路灯', '点位名': 'DRSU4', ...},
         {'序号': 5, '类型': '路灯', '点位名': 'DRSU5', ...}]
        """
        csv_name = f'drsu_{self.proj_name}.csv'
        # 保存文件的路径直接
        data_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
        csv_path = os.path.join(data_root, csv_name)

        logger.debug(f'项目：{self.proj_name}, '
                     f'配置文件：{csv_path}, 解析列：{self.columns}')

        if not os.path.exists(csv_path):
            logger.error(f'项目"{self.proj_name}"配置文件没有找到')
            return []

        drsu_list = []
        try:
            df = pd.read_csv(csv_path, sep=',', usecols=self.columns)
            sorted_df = df.sort_values(by='序号', )
            sorted_df_dict = sorted_df.T.to_dict()
            drsu_list = list(sorted_df_dict.values())
        except Exception as e:
            logger.error(str(e))
        finally:
            return drsu_list


class DRSUInfo(object):
    def __init__(self, project=None, columns=None):
        if not project:
            self.proj = const.PROJECT_NAME
        else:
            if isinstance(project, str):
                self.proj = [project]
            elif isinstance(project, list):
                self.proj = project
            else:
                logger.error('不支持的project参数格式，自动读取const中的配置')
                self.proj = const.PROJECT_NAME
        self._drsu_info = {}
        self.columns = columns

    def proj_drsu_params(self):
        """
        Input: 项目名称列表
        Output: {'proj1': [drsu_data_dict1, drsu_data_dict2, ...],
                 'proj2': [drsu_data_dict1, drsu_data_dict2, ...]'}
        """
        proj_drsu_dict = {}
        for proj in self.proj:
            drsu_list = ProjectInfo(proj, self.columns).drsu_list
            proj_drsu_dict.update({proj: drsu_list})
        return proj_drsu_dict

    @property
    def info(self):
        if not self._drsu_info:
            self._drsu_info = self.proj_drsu_params()
        return self._drsu_info


if __name__ == '__main__':
    a = DRSUInfo().info
    print(a)