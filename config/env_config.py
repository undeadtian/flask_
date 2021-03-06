# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 下午4:59
# @Author  : wth

import os
import collections
from configparser import ConfigParser


class Config:
    def __init__(self, config_file):
        """
        初始化
        config_file:待读取的配置文件名称
        """
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件:%s存在！" % self.conf_path)
        self.config.read(self.conf_path, encoding='utf-8')

    def get_sections(self):
        """
        获取配置文件的所有section
        :return:
        """
        return self.config.sections()

    def get_options(self, section_name):
        """
        获取指定section的所有option
        :param section_name:
        :return:
        """
        if self.config.has_section(section_name):
            return self.config.options(section_name)
        else:
            raise ValueError(section_name)

    def get_value(self, section, option):
        """
        获取字符串类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.config.get(section, option)

    def get_int(self, section, option):
        """
        获取整数类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.config.getint(section, option)

    def get_float(self, section, option):
        """
        获取浮点类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        """
        获取布尔类型的选项值
        :param section:
        :param option:
        :return:
        """
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        """
        获取内置类型的选项值
        :param section:
        :param option:
        :return:
        """
        return eval(self.config.get(section, option))

    @staticmethod
    def write_value(filename, data):
        """
        定义一个写入配置文件的方法
        :param filename: 配置文件名
        :param data: 嵌套字典的字典，键为区域名，嵌套的区域值为选项名和选项值的字典
        :return:
        """
        config = ConfigParser()
        if isinstance(data, dict):
            for key in data:
                config[key] = data[key]
            # 创建一个配置文件并将获取到的配置信息使用配置文件对象的写入方法进行写入
            with open(filename, mode='w', encoding='utf-8') as f:
                config.write(f)

    def add_value(self, dict_data):
        """
        定义一个写入配置文件的方法
        :param filename: 配置文件名
        :param data: 嵌套字典的字典，键为区域名，嵌套的区域值为选项名和选项值的字典
        :return:
        """
        if isinstance(dict_data, dict):
            for key, value in dict_data.items():
                for key1, value1 in value.items():
                    self.config.set(key, key1, value1)
            # 创建一个配置文件并将获取到的配置信息使用配置文件对象的写入方法进行写入
            self._update_cfg_file()

    def add_new_section(self, section_name):
        """
        增加section
        :param section_name:
        :return:
        """
        if not self.config.has_section(section_name):
            self.config.add_section(section_name)
            self._update_cfg_file()

    def add_option(self, section_name, option_key, option_value):
        """
        增加指定section下option
        :param section_name:
        :param option_key:
        :param option_value:
        :return:
        """
        if self.config.has_section(section_name):
            self.config.set(section_name, option_key, option_value)
            self._update_cfg_file()

    def del_section(self, section_name):
        """
        删除指定section
        :param section_name:
        :return:
        """
        if self.config.has_section(section_name):
            self.config.remove_section(section_name)
            self._update_cfg_file()

    def del_option(self, section_name, option_name):
        """
        删除指定section下的option
        :param section_name:
        :param option_name:
        :return:
        """
        if self.config.has_option(section_name, option_name):
            self.config.remove_option(section_name, option_name)
            self._update_cfg_file()

    def _update_cfg_file(self):
        with open(self.conf_path, "w") as f:
            self.config.write(f)


class EnvConfig(Config):
    def __init__(self, config_file='env_config.ini'):
        super().__init__(config_file)
        self._section = 'cali_env'
        self._cali_path = None
        self._fixed_path = None
        self._root_path = None
        self._resource_path = None
        self._tar_path = None
        self._local_host = None
        self._local_port = None
        self._remote_host = None
        self._remote_port = None
        self._user_name = None
        self._password = None
        self._remote_path = None

    @property
    def cali_path(self):
        if not self._cali_path:
            self._cali_path = self.get_value(self._section, 'cali_path')
        return self._cali_path

    @property
    def fixed_path(self):
        if not self._fixed_path:
            self._fixed_path = self.get_value(self._section, 'fixed_path')
        return self._fixed_path

    @property
    def root_path(self):
        if not self._root_path:
            self._root_path = self.get_value(self._section, 'root_path')
        return self._root_path

    @property
    def resource_path(self):
        if not self._resource_path:
            self._resource_path = self.get_value(self._section, 'resource_path')
        return self._resource_path

    @property
    def tar_path(self):
        if not self._tar_path:
            self._tar_path = self.get_value(self._section, 'tar_path')
        return self._tar_path

    @property
    def remote_host(self):
        if not self._remote_host:
            self._remote_host = self.get_value(self._section, 'remote_host')
        return self._remote_host

    @property
    def remote_port(self):
        if not self._remote_port:
            self._remote_port = self.get_value(self._section, 'remote_port')
        return self._remote_port

    @property
    def remote_path(self):
        if not self._remote_path:
            self._remote_path = self.get_value(self._section, 'remote_path')
        return self._remote_path

    @property
    def user_name(self):
        if not self._user_name:
            self._user_name = self.get_value(self._section, 'user_name')
        return self._user_name

    @property
    def password(self):
        if not self._password:
            self._password = self.get_value(self._section, 'password')
        return self._password

    @property
    def local_host(self):
        if not self._local_host:
            self._local_host = self.get_value(self._section, 'local_host')
        return self._local_host

    @property
    def local_port(self):
        if not self._local_port:
            self._local_port = self.get_value(self._section, 'local_port')
        return self._local_port


def config_manger(section, config_file='env_config.ini'):
    sections = Config(config_file).get_sections()
    dict_config = {'cali_env': EnvConfig}
    dict_config = collections.defaultdict({'cali_env': EnvConfig})
    if section in sections:
        return EnvConfig


if __name__ == '__main__':
    a = EnvConfig().remote_path
    print(a)
