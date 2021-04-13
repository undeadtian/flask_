# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 下午7:28
# @Author  : wth

import uuid
import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import io
import cv2
import subprocess
import shutil
import socket
import commands
from PIL import Image
import collections
from common.Log import Logger
from cali_config import CaliConfig
import socket
import threading
from config.constant import const
from calibration_control import CalibrationControl, CalibrationControlSingleton

# configuration
DEBUG = True
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

logger = Logger('calibration').getlog()


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in
               ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def check_conf_file(file_path):
    if not os.path.exists(file_path):
        if not os.path.exists(os.path.dirname(file_path)):
            os.mkdir(os.path.dirname(file_path))
        src_file = '/home/wth/fabu/calibration-master_t/conf/fixed_cam_calib.conf'
        shutil.copy(src_file, file_path)


def cover_mat(drsu_name, file_name='front_left'):
    dst_file = '/home/wth/fabu/calibration-master_t/data/calibration/resources/{}/camera/{}'.format(drsu_name, file_name)
    src_file_name = 'FrontRight' if file_name == 'front_right' else 'FrontLeft'
    src_file = '/home/wth/fabu/calibration-master_t/data/calibration/Lidar(Main)_to_Camera({})_manual_adjust'.format(
        src_file_name)
    shutil.copy(src_file, dst_file)
    logger.info('params cover, dst_file:{}'.format(dst_file))


def start_cali(drsu_name):

    command = "cd /home/wth/fabu/calibration-master_t/; pwd; ./scripts/fixed_cam_calib.sh  {}".format(
        drsu_name)
    command1 = "ps aux| grep fixed_cam_calib | grep -v grep | awk '{print $2}' | xargs kill -9"
    # command2 = "ps -aux | grep 'fixed_cam_calib.sh' | grep -v grep | wc -l"
    subprocess.call(command1, shell=True)
    subprocess.call(command, shell=True)


def cali_post(request_info):
    response_object = {'status': 'success'}
    post_data = request_info.get_json()
    id = uuid.uuid4().hex
    drsu_name = post_data.get('drsu_name')
    # file_path = '/home/wth/fabu/calibration-master_t/conf/{}/fixed_cam_calib.conf'.format(drsu_name)
    # check_conf_file(file_path)
    file_path = '/home/wth/fabu/calibration-master_t/conf/fixed_cam_calib.conf'
    cali_config = CaliConfig(file_path)
    cali_config.mod_params(post_data)
    if 'calibrate' == post_data.get('mode'):
        process_mode = [const.MODE_CALIBRETE]
    elif 'merge' == post_data.get('mode'):
        process_mode = [const.MODE_FILTER_1, const.MODE_CALIBRETE]
    elif 'filter' == post_data.get('mode'):
        process_mode = [const.MODE_FILTER, const.MODE_CALIBRETE]
    else:
        return jsonify({'status': 'fail'})
    cali_connect = CalibrationControlSingleton(drsu_name)
    for i in process_mode:
        cali_connect.send_msg(i)
        cali_connect.recv_msg()
    if const.MODE_CALIBRETE in process_mode:
        file_name = 'front_left' if post_data.get('device_id') == 'CameraFrontLeft' else 'front_right'
        logger.info('{}外参覆盖'.format(file_name))
        cover_mat(drsu_name, file_name)
    return jsonify(response_object)


def cali_get(request_info):
    get_data = request_info.get_json()
    # img_url = basedir + '/static/new.jpg'
    picture_name = 'new.jpg'
    picture_path = '/home/wth/fabu/calibration-master_t/picture'
    img_url = os.path.join(picture_path, picture_name)
    with open(img_url, 'rb') as f:
        a = f.read()
    # '''对读取的图片进行处理'''
    img_stream = io.BytesIO(a)
    img = Image.open(img_stream)
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    # print(imgByteArr)
    return imgByteArr


@app.route('/calibration2', methods=['GET', 'POST'])
@app.route('/calibration1', methods=['GET', 'POST'])
@app.route('/calibration', methods=['GET', 'POST'])
def calibration():
    if request.method == 'POST':
        return cali_post(request)
    else:
        return cali_get(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000, threaded=True)
    # recv_str = client.recv(1024)
    # recv_str = recv_str.decode("ascii")
    # print(recv_str)
