# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define('port', default=8000, type=int)


class IndexView(tornado.web.RequestHandler):
    def get(self):
        self.write('oo')


if __name__ == '__main__':
    # 装换命令行的参数，并保存到tornado.options.optrons
    tornado.options.parse_config_file('config.py')
    app = tornado.web.Application([(r'/', IndexView)])
    # app.listen(8000)
    # 手动创建服务器（手动一个http服务器对象）
    httpServer = tornado.httpserver.HTTPServer(app)
    # 监听端口
    # httpServer.listen(8000)
    httpServer.bind(tornado.options.options.port)
    # 默认是单进程的
    # 参数为None或为负数开进程个数为启硬件cpu的核数
    httpServer.start()
    tornado.ioloop.IOLoop.current().start()
# -*- coding: utf-8 -*-
