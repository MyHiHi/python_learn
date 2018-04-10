import tornado.web
import tornado.ioloop
import config

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello P')
if __name__=='__main__':
    app = tornado.web.Application([
        ('/',IndexHandler),
    ])
    app.listen(config.options.get('port'))
    tornado.ioloop.IOLoop.current().start()