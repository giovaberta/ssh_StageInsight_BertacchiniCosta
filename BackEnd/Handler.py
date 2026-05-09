import tornado.web, hashlib, json
import sys , os
from bson.objectid import ObjectId

#from ssh_StageInsight_BertacchiniCosta.global_var import user, Current_user

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from global_var  import *

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user_id")
    def write_msg(self,msg,status = 200):
        self.set_status(status)
        self.write(msg)
    def write_err(self,error,status = 500):
        self.set_status(status)
        self.write({"error": str(error)})

# Handler che renderizza la pagina principale per il login
class MainHandler(BaseHandler):
    def get(self):
        self.render("../frontend/login.html", error_message = None)

# Handler che gestisce il login degli utenti
class LoginHandler(BaseHandler):
    async def post(self):
        global Current_user
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


        self.set_secure_cookie("user_id", str(Utente["_id"]))


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
        self.write_msg({"success": "User created successfully"}, 201)


class GuestHandler(BaseHandler):
    def get(self):
        self.render("../frontend/guest.html")

class StudentHandler(BaseHandler):
    def get(self):
        self.render("../frontend/user.html")

    async def post(self):
        self.set_header("Content-Type", "application/json")

        user_id = self.get_current_user()
        if user_id is None:
            self.write_err("Unauthorized: user not logged in", 401)
            return

        Current_user = await user.find_one({"_id": ObjectId(user_id.decode())})
        if Current_user is None:
            self.write_err("User not found", 404)
            return

        try:
            # Legge il body JSON invece di form-urlencoded
            data = tornado.escape.json_decode(self.request.body)
        except Exception:
            self.write_err("Invalid JSON body", 400)
            return

        for field_name, arg in data.items():
            if not isinstance(arg, str) or arg.strip() == "":
                self.write_err(f"Valore mancante per il campo '{field_name}'", 400)
                return

            # Recupera la domanda dal DB tramite indice (domanda_1, domanda_2...)
            index = int(field_name.split("_")[1]) - 1
            domande = await form.find().to_list(length=None)

            if index >= len(domande):
                self.write_err(f"Domanda '{field_name}' non trovata", 404)
                return

            question = domande[index]

            await form.update_one(
                {"_id": question["_id"]},
                {"$set": {f"dati_ets.risp.{str(Current_user['_id'])}": arg.strip()}}
            )

        self.write_msg({"success": "Questionario inviato con successo"}, 200)

class UserListHandler(BaseHandler):
    async def get(self):
        self.set_header("Content-Type", "application/json")

        user_id = self.get_current_user()
        if user_id is None:
            self.write_err("Unauthorized", 401)
            return

        try:
            # Recupera tutti gli utenti dal DB
            utenti = await user.find().to_list(length=None)

            type_map = {0: "Admin", 1: "Guest", 2: "Student"}

            risultato = []
            for u in utenti:
                risultato.append({
                    "id": str(u["_id"]),
                    "email": u["email"],
                    "type": type_map.get(int(u["type"]), "Unknown")
                })


            self.write({"users": risultato})
        except Exception as ex:
            self.write_err(ex)

    async def delete(self):
        self.set_header("Content-Type", "application/json")

        user_id = self.get_current_user()
        if user_id is None:
            self.write_err("Unauthorized", 401)
            return

        try:
            data = tornado.escape.json_decode(self.request.body)
            target_id = data.get("id")
            if not target_id:
                self.write_err("Missing user id", 400)
                return

            result = await user.delete_one({"_id": ObjectId(target_id)})
            if result.deleted_count == 0:
                self.write_err("User not found", 404)
                return

            self.write_msg({"success": "User deleted"}, 200)
        except Exception as ex:
            self.write_err(str(ex))


class NewStudentHandler(BaseHandler):
    def get(self):
        self.render("../frontend/nuovoutente.html")

    def post(self):
        pass

class FormHandler(BaseHandler):
    async def get(self):
        # Se la richiesta vuole JSON (fetch dal JS), restituisce le domande
        if "application/json" in self.request.headers.get("Accept", ""):
            await self.get_questions()
        else:
            self.render("../frontend/modificaquestionario.html")

    async def get_questions(self):
        self.set_header("Content-Type", "application/json")

        user_id = self.get_current_user()
        if user_id is None:
            self.write_err("Unauthorized", 401)
            return
        #print("DEBUG user_id:", user_id)
        try:
            domande = form.find()
            risultato = []
            async for d in domande:
                #print(d)
                keys = d.keys()
                print(list(keys)[1])
                f = d[list(keys)[1]]
                risultato.append(
                    {
                        "testo_domanda": d.get("testo_domanda", ""),
                        "tipo_risposta": f["type"],
                        "opzioni": f.get("possible_risp" ,[])
                    })


            print("DEBUG risultato:", risultato)
            self.write(json.dumps(risultato))

        except Exception as ex:
            print("DEBUG eccezione:", ex)
            self.write_err(str(ex))

    async def post(self):
        self.set_header("Content-Type", "application/json")

        user_id = self.get_current_user()
        if user_id is None:
            self.write_err("Unauthorized", 401)
            return

        testo_domanda = self.get_argument("testo_domanda", "").strip()
        tipo_risposta = self.get_argument("tipo_risposta", "").strip()

        if not testo_domanda or not tipo_risposta:
            self.write_err("Campi mancanti", 400)
            return

        # Controlla se la domanda esiste già
        existing = await form.find_one({"testo_domanda": testo_domanda})
        if existing:
            self.write_err("Domanda già esistente", 409)
            return

        try:
            await form.insert_one({
                "testo_domanda": testo_domanda,
                "tipo_risposta": tipo_risposta,
                "dati_ets": {"risp": {}}  # struttura per le risposte degli studenti
            })
            self.write_msg({"success": "Domanda salvata"}, 201)
        except Exception as ex:
            self.write_err(str(ex))

    async def delete(self):
        self.set_header("Content-Type", "application/json")

        user_id = self.get_current_user()
        if user_id is None:
            self.write_err("Unauthorized", 401)
            return

        testo_domanda = self.get_argument("testo_domanda", "").strip()
        tipo_risposta = self.get_argument("tipo_risposta", "").strip()

        if not testo_domanda:
            self.write_err("Testo domanda mancante", 400)
            return

        try:
            result = await form.delete_one({
                "testo_domanda": testo_domanda,
                "tipo_risposta": tipo_risposta
            })
            if result.deleted_count == 0:
                self.write_err("Domanda non trovata", 404)
                return

            self.write_msg({"success": "Domanda eliminata"}, 200)
        except Exception as ex:
            self.write_err(str(ex))