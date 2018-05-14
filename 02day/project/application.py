# -*- coding: utf-8 -*-
from tornado.web import Application, url
from views.index import IndexHandler, HomeHandler, JsonHandler, JsonHandler2, RedirectHandler, ErrorHandler, \
    KaigeHandler, LyfHandler, ArgumentHandler, ArgumentsHandler,PostfileHandler,UpfileHandler
import config


class Application(Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/home', HomeHandler, {'world1': "one", "world2": "tow"}),
            (r'/json', JsonHandler),
            (r'/json2', JsonHandler2),
            (r'/index', RedirectHandler),
            (r'/iserror', ErrorHandler),
            # 反向解析
            url(r'/kaige', KaigeHandler, {'world3': "tree", "world4": "four"}, name='kaige'),
            (r'/lyf/(?P<p1>\w+)/(?P<p2>\w+)/(?P<p3>\w+)', LyfHandler),
            url(r'/argument', ArgumentHandler),
            url(r'/arguments', ArgumentsHandler),

            url(r'/postfile', PostfileHandler),
            url(r'/upfile', UpfileHandler),


        ]
        super(Application, self).__init__(handlers, **config.settings)
