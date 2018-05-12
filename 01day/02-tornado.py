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
    # 手动创建服务器
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)
    tornado.ioloop.IOLoop.current().start()
