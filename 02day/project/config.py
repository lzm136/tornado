# -*- coding: utf-8 -*-
import os

# 当前文件路径
BASE_DIRS = os.path.dirname(__file__)

# 参数
options = {
    "port": 8080,
    "list": ['good', 'nice']
}

settings = {
    'debug': True,
    # 静态文件的路径
    'static': os.path.join(BASE_DIRS, 'static'),
    # 模板的路径
    'template': os.path.join(BASE_DIRS, 'template')
}
