# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 下午3:33
# @Author  : wth
import time
from proto import lidar_camera_cross_calibration_config_pb2
from proto import sensor_source_pb2
from google.protobuf import text_format
from google.protobuf.json_format import MessageToJson
from common.Log import Logger

logger = Logger('CaliConfig').getlog()


class CaliConfig(object):

    def __init__(self, src_file, dest_file=None):
        """
        Args:
            src_file: 读取配置文件地址
            dest_file: 保存配置文件地址
        """
        self._conf_file = src_file
        self._save_file = dest_file if dest_file else src_file
        self._config = self._get_conf()

    def _save_conf(self):
        with open(self._save_file, "w+") as f:
            f.write(text_format.MessageToString(self._config))

    # 只对filter的中间结果备份
    def _bk_conf(self, mode, device_id):
        if mode != 'filter':
            return
        rq = time.strftime("%Y%m%d%H%M", time.localtime())
        if device_id == 'CameraFrontRight':
            text = f'front_right_{rq}'
        elif device_id == 'CameraFrontLeft':
            text = f'front_left_{rq}'
        else:
            logger.warning(f'device_id 错误：{device_id}')
            return
        with open(self._save_file.replace('.', f'{text}.'), 'w+') as f:
            f.write(text_format.MessageToString(self._config))

    def _get_conf(self):
        with open(self._conf_file, 'r') as f:
            message = f.read()
        return text_format.Parse(message, lidar_camera_cross_calibration_config_pb2.LidarCameraCrossCalibration())

    def mod_calib_params_adj(self, post_data):
        tmp_config = self._config.calib_params_adjustment
        tmp_config.set_init_parameters = post_data.get('set_init_parameters')
        tmp_config.calib_init_params.rotate_x = float(post_data.get('rotate_x'))
        tmp_config.calib_init_params.rotate_y = float(post_data.get('rotate_y'))
        tmp_config.calib_init_params.rotate_z = float(post_data.get('rotate_z'))
        tmp_config.calib_init_params.x = float(post_data.get('x'))
        tmp_config.calib_init_params.y = float(post_data.get('y'))
        tmp_config.calib_init_params.z = float(post_data.get('z'))
        tmp_config.calib_init_params.camera_origin_distance = float(post_data.get('camera_origin_distance'))
        tmp_config.camera_pitch_adjustment = float(post_data.get('camera_pitch_adjustment'))
        tmp_config.camera_yaw_adjustment = float(post_data.get('camera_yaw_adjustment'))
        tmp_config.camera_roll_adjustment = float(post_data.get('camera_roll_adjustment'))
        tmp_config.x_adjustment_along_lidar = float(post_data.get('x_adjustment_along_lidar'))
        tmp_config.y_adjustment_along_lidar = float(post_data.get('y_adjustment_along_lidar'))
        tmp_config.z_adjustment_along_lidar = float(post_data.get('z_adjustment_along_lidar'))

    def mod_lidar_config(self, post_data):
        tmp_config = self._config.lidar_config
        tmp_config.enable_range = post_data.get('enable_range')
        tmp_config.x_gamma = float(post_data.get('x_gamma'))
        tmp_config.depth_diff_cap = float(post_data.get('depth_diff_cap'))
        tmp_config.min_range_diff = float(post_data.get('min_range_diff'))
        tmp_config.low_depth_diff_filter = float(post_data.get('low_depth_diff_filter'))
        tmp_config.penalty_from_range_coeff = float(post_data.get('penalty_from_range_coeff'))
        tmp_config.min_range = float(post_data.get('min_range'))
        tmp_config.constrain_range_area = post_data.get('constrain_range_area')
        tmp_config.range_y_max_margin = float(post_data.get('range_y_max_margin'))
        tmp_config.range_y_min_margin = float(post_data.get('range_y_min_margin'))
        tmp_config.range_max_ego_x = float(post_data.get('range_max_ego_x'))
        tmp_config.range_min_ego_x = float(post_data.get('range_min_ego_x'))
        tmp_config.range_max_ego_z = float(post_data.get('range_max_ego_z'))
        tmp_config.range_min_ego_z = float(post_data.get('range_min_ego_z'))
        tmp_config.enable_intensity = post_data.get('enable_intensity')
        tmp_config.min_intensity_diff = float(post_data.get('min_intensity_diff'))
        tmp_config.intensity_weight = float(post_data.get('intensity_weight'))
        tmp_config.intensity_max_limit = float(post_data.get('intensity_max_limit'))
        tmp_config.intensity_min_limit = float(post_data.get('intensity_min_limit'))
        tmp_config.intensity_max_ego_z = float(post_data.get('intensity_max_ego_z'))
        tmp_config.intensity_min_ego_z = float(post_data.get('intensity_min_ego_z'))
        tmp_config.constrain_intensity_area = post_data.get('constrain_intensity_area')
        tmp_config.intensity_y_max_margin = float(post_data.get('intensity_y_max_margin'))
        tmp_config.intensity_y_min_margin = float(post_data.get('intensity_y_min_margin'))
        tmp_config.intensity_max_ego_x = float(post_data.get('intensity_max_ego_x'))
        tmp_config.intensity_min_ego_x = float(post_data.get('intensity_min_ego_x'))
        tmp_config.min_range = float(post_data.get('min_range'))

    def mode_device_id(self, device_id):
        if device_id == 'CameraFrontRight':
            device_id = sensor_source_pb2.CameraFrontRight
        elif device_id == 'CameraFrontLeft':
            device_id = sensor_source_pb2.CameraFrontLeft
        else:
            logger.warning('错误的device_id:{}'.format(device_id))
            return
        if self._config.camera_config.device_id != device_id:
            self._config.camera_config.device_id = device_id

    def mod_params(self, post_data):
        mode = post_data.get('mode')
        device_id = post_data.get('device_id')
        if mode == 'calibrate':
            self.mod_calib_params_adj(post_data)
        elif mode == 'filter':
            self.mod_lidar_config(post_data)
        elif mode == 'merge':
            return
        else:
            pass
        self.mode_device_id(device_id)
        self._bk_conf(mode, device_id)
        self._save_conf()

    @property
    def cali_config(self):
        json_obj = MessageToJson(self._config)
        return json_obj



# def ModConf():

if __name__ == '__main__':
    # getConf()
    A = CaliConfig()
