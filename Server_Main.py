import tornado,pymongo,asyncio
from global_var import *
from BackEnd.Handler import *


def make_up():
    return tornado.web.Application([
        (r"/",MainHandler),
        (r"/login",LoginHandler),
        (r"/admin",AdminHandler),
        (r"/admin/newus",NewStudentHandler),
        (r"/guest",GuestHandler),
        (r"/student",StudentHandler),
        (r"/newstudent",NewStudentHandler),
        (r"/form",FormHandler),
        (r"/users", UserListHandler),
        (r"/frontend/(.*)", tornado.web.StaticFileHandler, {"path": "frontend"})
        ],
        debug = True,
        static_path = os.path.join(os.path.dirname(__file__), "frontend"),
        cookie_secret = "utente_che_si_logga"
    )

async def main(shutdown_event):
    app = make_up()
    app.listen(port_listener)
    print(f"Listen at URL: http://localhost:{port_listener}")
    await shutdown_event.wait()

# Codice main
if __name__ == "__main__":
    # Evento asincrono per fermare in maniera "gentile" l'applicazione web
    shutdown_event = asyncio.Event()
    try:
        # Mando in esecuzione l'applicazione
        asyncio.run(main(shutdown_event))
    except KeyboardInterrupt:
        # Se viene rilevato un KeyboardInterrupt (ctrl+c) e viene arrestato in maniera "gentile"
        print("Shutting down")
        shutdown_event.set()
    except Exception as e:
        # Se si presenta un errore di qualsiasi altro tipo lo catturo e lo stampo, per capire che errore si è generato
        print(f"Critical error: {e}")
        # Arresto l'applicazione in maniera "gentile"
        shutdown_event.set()
