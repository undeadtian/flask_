# -*- coding: utf-8 -*-
# @DateTime : 2021/4/12-上午10:56
# @Author   : byron
import os
import pandas as pd


class DRSUCaliControl(object):
    def __init__(self, data_root, logger):
        self.data_root = data_root
        self.logger = logger

    def _parse_proj_csv(self, proj_name, columns=None):
        """
        Input: columns: 需要抽取的数据列名称列表
        Output: drsu_list:
        [{'序号': 1, '类型': '路灯', '点位名': 'DRSU1', ...},
         {'序号': 4, '类型': '路灯', '点位名': 'DRSU4', ...},
         {'序号': 5, '类型': '路灯', '点位名': 'DRSU5', ...}]
        """
        csv_name = f'drsu_{proj_name}.csv'
        csv_path = os.path.join(self.data_root, csv_name)
        columns_default = ['序号', '类型', '点位名']
        columns = columns if columns else columns_default

        self.logger.debug(f'项目：{proj_name}, '
                          f'配置文件：{csv_path}, 解析列：{columns}')

        if not os.path.exists(csv_path):
            self.logger.error(f'项目"{proj_name}"配置文件没有找到')
            return []

        drsu_list = []
        try:
            df = pd.read_csv(csv_path, sep=',', usecols=columns)
            sorted_df = df.sort_values(by='序号', )
            sorted_df_dict = sorted_df.T.to_dict()
            drsu_list = list(sorted_df_dict.values())
        except Exception as e:
            self.logger.error(str(e))
        finally:
            return drsu_list

    def proj_drsu_params(self, proj_list):
        """
        Input: 项目名称列表
        Output: {'proj1': [drsu_data_dict1, drsu_data_dict2, ...],
                 'proj2': [drsu_data_dict1, drsu_data_dict2, ...]'}
        """
        self.logger.info("解析项目drsu参数")
        if not proj_list or not type(proj_list) == list:
            self.logger.warning("输入项目列表为空")
            return
        self.logger.info(f'当前项目：{proj_list}')
        proj_drsu_dict = {}
        for proj in proj_list:
            drsu_list = self._parse_proj_csv(proj)
            proj_drsu_dict.update({proj: drsu_list})

        return proj_drsu_dict
