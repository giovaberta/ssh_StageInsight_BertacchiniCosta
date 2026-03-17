import tornado.web, hashlib
import sys , os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from global_var  import *


class BaseHandler(tornado.web.RequestHandler):
    def write_msg(self,msg,status = 200):
        self.set_status(status)
        self.write(msg)
    def write_err(self,error,status = 500):
        self.set_status(status)
        self.write({"error": error})

# Handler che renderizza la pagina principale per il login
class MainHandler(BaseHandler):
    def get(self):
        self.render("../frontend/login.html")

# Handler che gestisce il login degli utenti
class LoginHandler(BaseHandler):
    async def post(self):
        self.set_header("Content-Type", "application/json")

        email = self.get_argument("email")
        pwd = self.get_argument("password")
        # Oggetto di tipo hashlib con criptazione sha3 512
        pwd_cript = hashlib.sha3_512(pwd.encode(),usedforsecurity=True)

        if email == "" or pwd == "":
            self.write_err("Password or email missing",400)
            return

        try:
            Utente =  await user.find_one({"email":email})
        except Exception as ex:
            self.write_err(ex)
            return

        if Utente == None:
            self.write_err("User not found",401)
            return

        if not Utente["pwd"] == pwd_cript.hexdigest():
            self.write_err("Password doesn't match",401)
            return

        self.set_status(200)
        if Utente["type"] == 0:
            self.redirect(f"/admin?id={Utente['_id']}")
        elif Utente["type"] == 1:
            self.redirect(f"/guest?id={Utente['_id']}")
        elif Utente["type"] == 2:
            self.redirect(f"/student?id={Utente['_id']}")
        else:
            self.write_err("Type not supported",404)

class AdminHandler(BaseHandler):
    pass

class GuestHandler(BaseHandler):
    pass

class StudentHandler(BaseHandler):
    pass
