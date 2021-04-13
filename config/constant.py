# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 下午5:04
# @Author  : wth

class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value


const = _const()

const.MODE_CALIBRETE = 3
const.MODE_FILTER = 2
const.MODE_MERGE = 1
const.MODE_FILTER_1 = 4
const.PROJECT_NAME = {'xiaoshan': 'xz', 'jichang': 'jc', 'wuzhen': 'wz'}