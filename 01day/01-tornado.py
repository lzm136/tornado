# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello wold')


if __name__ == '__main__':
    # url
    app = tornado.web.Application([(r'/', IndexHandler)])
    # 端口
    app.listen(8800)
    # 启动方式
    tornado.ioloop.IOLoop.current().start()
