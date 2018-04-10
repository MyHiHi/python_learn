# coding=utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hihi')

tornado.options.define('port',default=8000,type=int)
tornado.options.define('port_list',default=[],type=str,multiple=True)
if __name__=='__main__':
    # 从命令行转换参数
    # tornado.options.parse_command_line()
    # 从配置文件转换参数
    tornado.options.parse_config_file('config')
    app = tornado.web.Application([
        ('/',HomeHandler)
    ])
    print 'list = {}'.format(tornado.options.options.port_list)
    # app.listen(8003)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start()
    # tornado.ioloop.IOLoop.current().start()
    tornado.ioloop.IOLoop.current().start()