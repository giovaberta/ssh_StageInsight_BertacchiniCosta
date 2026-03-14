import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def write_msg(self,msg,status = 200):
        self.set_status(status)
        self.write(msg)
    def write_err(self,error,status = 500):
        self.set_status(status)
        self.write(error)

class MainHandler(BaseHandler):
    def get(self):
        self.render("../frontend/home.html")

    def post(self):
        self.set_header("Content-Type", "application/json")

        data = tornado.escape.json_decode(self.request.body)
        self.write_msg(data)