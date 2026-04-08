import tornado.web, hashlib
import sys , os

#from ssh_StageInsight_BertacchiniCosta.global_var import user, Current_user

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
        self.render("../frontend/login.html", error_message = None)

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
            #self.redirect("../frontend/login.html", error_message="Username o Password errati!")
            self.write_err("Username o Password errati!")
            return

        if not Utente["pwd"] == pwd_cript.hexdigest():
            self.write_err("Password doesn't match",401)
            return

        Current_user = Utente

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
    def get(self):
        self.render("../frontend/adminboss.html")

    async def post(self):
        self.set_header("Content-Type", "application/json")
        email = self.get_argument("email")
        pwd = self.get_argument("pwd")
        type_user = self.get_argument("type")
        alredy_exist = await  user.find_one({"email":email})
        if alredy_exist:
            self.write_err("Email already exists",409)
            return
        ins = await user.insert_one({"email":email,"pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":type_user})
        if not ins:
            self.write_err("DataBase error",401)
            return



class GuestHandler(BaseHandler):
    def get(self):
        self.render("../frontend/guest.html")

class StudentHandler(BaseHandler):
    def get(self):
        self.render("../frontend/user.html")

    async def post(self):
        self.set_header("Content-Type", "application/json")
        keys = list(self.request.body_arguments.keys())
        for key in keys:
            print(key)

            arg = self.get_argument(key).strip(" ")
            print(arg)
            if arg == "":
                self.write_err("Missing argument",401)
            # Controllo che la domanda esista e la prendo con tutto il suo contenuto
            question = await form.find_one({key : {"$exists" : True}})
            if question == None:
                self.write_err("Critical error")
            print(question)
            #question[str(Current_user["_id"])] = arg
            #await form.upgrade({key:question})

class NewStudentHandler(BaseHandler):
    def get(self):
        self.render("../frontend/nuovoutente.html")

    def post(self):
        pass