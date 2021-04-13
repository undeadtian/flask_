# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 下午3:28
# @Author  : wth
import os
import subprocess
from ssh.base_command import BaseCommand
from common.Log import Logger
from config.constant import const

logger = Logger('DRSUEnv').getlog()


class DRSUEnv(object):
    def __init__(self, project_name, drsu_id, tar_dir, root_dir):
        self.project_name = project_name
        self.drsu_id = drsu_id
        self.tar_dir = self.check_dir(os.path.join(tar_dir, project_name))
        self.root_dir = root_dir
        self.tar_name = 'drsu{}.tar.gz'.format(str(self.drsu_id).rjust(2, '0'))
        # self.ssh_session = BaseCommand(host, port, username, password)
        # self.ssh_session.reconnect()  # 建立连接

    @staticmethod
    def check_dir(file_dir):
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
            logger.info('创建目录：{}'.format(file_dir))
        return file_dir

    def down_load_cali_data(self, host, port, remote_path, username='broadxt', password='broadxt333', ):
        """
        从服务器上下载压缩文件，download自动判断是否下载成功
        Args:
            host:服务器ip
            port:端口
            remote_path:远端文件夹绝对路径
            username:账号
            password:密码

        Returns:是否下载成功

        """
        ssh_session = BaseCommand(host, port, username, password)
        ssh_session.reconnect()
        remote_path = os.path.join(remote_path, self.project_name, self.tar_name)
        locate_path = os.path.join(self.tar_dir, self.tar_name)
        try:
            ssh_session.download(remote_path, locate_path)
            logger.info('压缩文件：{}下载到本地：{}成功'.format(remote_path,locate_path))
            return True
        except IOError:
            logger.error('压缩文件下载失败，请检查配置:\n remote_path:{},locate_path:{}'.format(remote_path, locate_path))
            return False

    def unzip_cali_data(self, ):
        """
        解压下载的压缩文件
        Returns:

        """
        tar_path = os.path.join(self.tar_dir, self.tar_name)
        command = 'tar -zvxf {} -C {}'.format(tar_path, os.path.join(self.root_dir, self.project_name))
        subprocess.run(command)
        logger.info('解压压缩文件：{}到{}文件夹'.format(tar_path, self.root_dir))

    # def copy_cali_data(self):
    def move_camera_conf(self):
        camera_conf_path = os.path.join(self.root_dir, self.project_name,
                                        'drsu{}'.format(str(self.drsu_id).rjust(2, '0')), 'front_*')
        drsu_name = '{}_drsu_{}'.format(const.PROJECT_NAME[self.project_name], str(self.drsu_id))
        dest_conf_path = os.path.join(os.path.dirname(self.root_dir), 'resources', drsu_name)
        command = 'mv {} {}'.format(camera_conf_path, dest_conf_path)
        subprocess.run(command)
        logger.info('将文件:{}拷贝到:{}'.format(camera_conf_path, dest_conf_path))


if __name__ == '__main__':
    A = DRSUEnv('xiaoshan', 1, '/home/broadxt/wth', '/home/wth/fabu/calibration-master/data/calibration/fixed_cam_calib')
    A.down_load_cali_data('172,16.4.112', 22, '/home/broadxt/xiaoshan/drsu_data')