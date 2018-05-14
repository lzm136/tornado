# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import json
import config
import os


class IndexHandler(RequestHandler):
    def get(self):
        url = self.reverse_url('kaige')
        self.write("<a href='%s'>去另一个页面</a>" % url)


class HomeHandler(RequestHandler):
    def initialize(self, world1, world2):
        self.world1 = world1
        self.world2 = world2

    def get(self):
        print(self.world1, self.world2)
        self.write('home llo')


class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            'name': 'json',
            'age': 20,
            'gender': '男',
            'height': 170
        }
        # 将字典转化成json
        jsonStr = json.dumps(per)
        self.write(jsonStr)


class JsonHandler2(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            'name': 'json',
            'age': 20,
            'gender': '男',
            'height': 170
        }
        self.write(per)
        self.set_header('content-type', 'application/json; charset=utf-8')


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')


class ErrorHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            code = 404
            self.write('连接失败')
        elif status_code == 500:
            code = 500
            self.write('服务器错误')
        self.set_status(code)

    def get(self, *args, **kwargs):
        flag = self.get_query_argument('flag')
        if flag == '0':
            self.send_error(500)
        self.write('you are right')


class KaigeHandler(RequestHandler):
    def initialize(self, world3, world4):
        self.world3 = world3
        self.world4 = world4

    def get(self, *args, **kwargs):
        print(self.world3, self.world4)
        self.write('kaige')


class LyfHandler(RequestHandler):
    def get(self, p1, p2, p3, *args, **kwargs):
        print(p1 + '-' + p2 + '-' + p3)
        self.write('lyf')


class ArgumentHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a')
        b = self.get_query_argument('b')
        c = self.get_query_argument('c')
        print(a, b, c)
        self.write('ArgumentHandler')


class ArgumentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        list = self.get_query_argument('a')
        print(list)
        self.write('ArgumentHandler')


class PostfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('../template/postfiled.html')

    def post(self, *args, **kwargs):
        name = self.get_body_argument('username')
        pwd = self.get_body_argument('pwd')
        hoby_list = self.get_body_arguments('hoby')
        print(name, pwd, hoby_list)
        self.write('success')


# {'file': [{'filename': 'a.txt', 'body': b'Abcd\n', 'content_type': 'text/plain'}, {'filename': 'b.txt', 'body': b'Abcd\n', 'content_type': 'text/plain'}]}
class UpfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('../template/upfile.html')

    def post(self, *args, **kwargs):
        fileDict = self.request.files
        for inputName in fileDict:
            fileArray = fileDict[inputName]
            for fileObject in fileArray:
                filePath = os.path.join(config.BASE_DIRS, 'upfile/' + fileObject.filename)
                with open(filePath, 'wb') as f:
                    f.write(fileObject.body)
        self.write('ok')
