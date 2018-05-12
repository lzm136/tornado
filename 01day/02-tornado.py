# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop


class IndexView(tornado.web.RequestHandler):
    def get(self):
        self.write('oo')


if __name__ == '__main__':
    app = tornado.web.Application([(r'', IndexView)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
