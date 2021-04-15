# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 下午2:13
# @Author  : wth
import socket
import time
import os
import threading
import subprocess
import datetime
from datetime import timedelta

from common.Log import Logger

logger = Logger('CalibrationControl').getlog()
MAX_RETRY_TIMES = 3


# 控制標定程序的python類，所有與標稱程序交互的動作都又該類完成
class CalibrationControlSingleton(object):
    instance = None
    init_flag = False

    # 單例模式，只需要給第一個對象分配空間
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, drsu_name, cali_dir, host='127.0.0.1', port=8000, root_dir='data/calibration/fixed_cam_calib'):
        if CalibrationControlSingleton.init_flag:
            return
        logger.info('初始化CalibrationControl')
        CalibrationControlSingleton.init_flag = True
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.remote_host = host
        self.cali_dir = cali_dir
        self.remote_port = int(port)
        self.drsu_name = drsu_name
        self.cali_p = None
        self.root_dir = root_dir
        self.try_times = MAX_RETRY_TIMES
        self._start_cali()
        self._connect()

    def _connect(self):
        if not self.cali_p:
            self._start_cali()
        while True:
            try:
                self.client.connect((self.remote_host, self.remote_port))
                logger.info('連接到標定程序，host：{}，port:{}'.format(self.remote_host, self.remote_port))
                return
            except Exception as e:
                if self.try_times != 0:
                    logger.warning(u'连接連接標定程序失敗失败host:{},port:{}，进行重试'.format(self.remote_host,
                                                                              self.remote_port))
                    self.try_times -= 1
                else:
                    logger.warning(u'重试{}次失败，结束程序'.format(MAX_RETRY_TIMES))
                    exit(1)

    def close(self):
        self.client.close()

    def send_msg(self, msg):
        # msg = MODE_CALIBRETE
        self.client.send(bytes(str(msg), encoding="ascii"))
        logger.info('send msg:{}'.format(msg))

    def recv_msg(self, wait_time):
        # wait_until = datetime.now() + timedelta(hours=delete_TO)
        while True:
            recv_str = self.client.recv(1024, 0)
            recv_str = recv_str.decode("ascii")
            if recv_str == 'Success':
                logger.info('recv msg success')
                break

    def send_msg_wait(self, msg, wait_time=0):
        self.send_msg(msg)
        self.recv_msg(wait_time)

    def get_cali_status(self):
        """
        获取标定程序状态
        """
        command = 'ps aux | grep "fixed_cam_calib/main" | grep -v grep | wc -l'
        result = subprocess.check_output(command, shell=True)
        result = result.decode()
        return result

    def _start_cali(self):
        command1 = "ps aux| grep fixed_cam_calib | grep -v grep | awk '{print $2}' | xargs kill -9"
        subprocess.call(command1, shell=True)
        command = "cd {}; pwd; ./scripts/fixed_cam_calib.sh {} {}".format(
            self.cali_dir, self.drsu_name, self.root_dir)
        # subprocess.call(command, shell=True)
        self.cali_p = subprocess.Popen(command, shell=True)
        time.sleep(10)
        logger.info("標定進程狀態：{}，進程pid:{}".format(self.cali_p.poll(), self.cali_p.pid))

    def restart_cali(self):
        self._start_cali()
        self._connect()

    def end_cali(self):
        if self.cali_p:
            self.cali_p.kill()
            # os.killpg(os.getpgid(self.cali_p.pi), 9)
            self.cali_p = None


if __name__ == '__main__':
    a = CalibrationControlSingleton('wz_drsu14', '/home/wth/fabu/calibration-master',
                                    root_dir='data/calibration/fixed_cam_calib/xiaoshan/drsu01')
    # print(a.get_cali_status())
    # a.restart_cali()
    a.send_msg(4)
    time.sleep(1000)
