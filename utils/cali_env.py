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
    def __init__(self, project_name, drsu_id, tar_dir, root_dir,
                 remote_host, remote_port, remote_path, froce, username='broadxt', password='broadxt333', ):
        """
        从远端服务器下载标定数据的压缩文件，解压后存放到标定程序文件夹中的指定路径下
        Args:
            project_name:项目名称 e.g:xiaoshan
            drsu_id:drsuid e.g:1
            tar_dir: 本地用与临时存放压缩文件的文件夹地址
            root_dir: 本地标定程序中存放标定数据的文件夹地址 一般位于标定文件下 data/calibration/fixed_cam_calib
            remote_host: 服务器ip
            remote_port: 服务器端口号
            remote_path: 服务器压缩文件所在文件夹地址
            username:
            password:
            force: 如果当前已经有环境，是否需要重新下载解压覆盖原有环境
        """
        self.project_name = project_name
        self.drsu_id = drsu_id
        self.remote_info = [remote_host, remote_port, username, password]
        self.remote_path = remote_path
        self.root_dir = root_dir
        self.force = froce
        self.tar_name = 'drsu{}.tar.gz'.format(str(self.drsu_id).rjust(2, '0'))
        self.tar_dir = self.check_dir(os.path.join(tar_dir, project_name))
        # self.ssh_session = BaseCommand(host, port, username, password)
        # self.ssh_session.reconnect()  # 建立连接

    @staticmethod
    def check_dir(file_dir):
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
            logger.info('创建目录：{}'.format(file_dir))
        return file_dir

    def down_load_cali_data(self):
        """
        从服务器上下载压缩文件，download自动判断是否下载成功
        Args:
        Returns:是否下载成功
        """
        ssh_session = BaseCommand(*self.remote_info)
        ssh_session.reconnect()
        remote_path = os.path.join(self.remote_path, self.project_name, self.tar_name)
        locate_path = os.path.join(self.tar_dir, self.tar_name)
        try:
            ssh_session.download(remote_path, locate_path)
            logger.info('压缩文件：{}下载到本地：{}成功'.format(remote_path, locate_path))
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

    def is_exist_cali_env(self):
        pass  # TODO 检查本地是否已经存在标定数据

    def prepare_for_cali_env(self):
        """
        标定环境准备
        Returns:
        """
        logger.info('开始准备本地标定环境，项目：{}，drsu:{}'.format(self.project_name, self.drsu_id))
        if not self.down_load_cali_data():
            logger.error('标定环境准备失败！')
            return False
        self.unzip_cali_data()
        self.move_camera_conf()
        logger.info('标定环境准备成功')
        return True


if __name__ == '__main__':
    A = DRSUEnv('xiaoshan', 1, '/home/broadxt/wth',
                '/home/wth/fabu/calibration-master/data/calibration/fixed_cam_calib',
                '172,16.4.112', 22, '/home/broadxt/xiaoshan/drsu_data')
    A.prepare_for_cali_env()
