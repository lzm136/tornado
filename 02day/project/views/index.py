# -*- coding: utf-8 -*-
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello lzm')
