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
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()
