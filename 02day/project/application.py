# -*- coding: utf-8 -*-
from tornado.web import Application
from views.index import IndexHandler
import config


class Application(Application):
    def __init__(self):
        handlers = [(r'/', IndexHandler)]
        super(Application).__init__(handlers)
