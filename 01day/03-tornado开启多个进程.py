# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexView(tornado.web.RequestHandler):
    def get(self):
        self.write('oo')


if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexView)])
    # app.listen(8000)
    # 手动创建服务器（手动一个http服务器对象）
    httpServer = tornado.httpserver.HTTPServer(app)
    # 监听端口
    # httpServer.listen(8000)
    httpServer.bind(8000)
    # 默认是单进程的
    # 参数为None或为负数开进程个数为启硬件cpu的核数
    httpServer.start(5)
    tornado.ioloop.IOLoop.current().start()
