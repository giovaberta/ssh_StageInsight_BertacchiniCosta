import tornado,pymongo,asyncio
from global_var import *
from backend.Handler import *


def make_up():
    return tornado.web.Application([
        (r"/",MainHandler),
        (r"/login",LoginHandler),
        (r"/admin",AdminHandler),
        (r"/guest",GuestHandler),
        (r"/student",StudentHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "frontend"})
        ],
        debug = True,
        static_path = "frontend",
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
