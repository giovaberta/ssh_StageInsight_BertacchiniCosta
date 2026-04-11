from global_var import *
import asyncio, hashlib
async def make_up():
    pwd = "prova"
    ut_admin = {"email":"prova@admin","pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":0}
    ut_user = {"email":"prova@user","pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":2}
    ut_guest = {"email":"prova@guest","pwd":hashlib.sha3_512(pwd.encode(),usedforsecurity=True).hexdigest(),"type":1}
    await user.insert_one(ut_admin)
    await user.insert_one(ut_user)
    await user.insert_one(ut_guest)


    await form.insert_many([
        {"dati_ets":{"type":"testo_breve","risp":{}}},
        {"dati_alunno":{"type":"testo_breve","risp":{}}},
        {"percorso_studente":{"type":"testo_breve","risp":{}}},
        {"prima_esperienza":{"type":"si_no","risp":{}}},
        {"fonte_info":{"type":"menu_tendina","risp":{},"possible_risp":["Progetto Cantieri Giovani","Dalla scuola","Dall'informagiovani","Dai centri giovani","Dal CSV Terre Estensi","Materiale promozionale","Servizi sociali","Dalla mia famiglia","Da un amico"]}},
        {"motivazioni":{"type":"scelta_multipla","risp":{},"possible_risp":["Il confronto con i miei insegnanti","Gli stimoli degli amici","Gli stimoli della mia famiglia","La curiosità di provare qualcosa di nuovo","Le mie convinzioni personali","Qualche cosa che mi è successo"]}}
    ])

    await form.insert_many([
        {"ruolo_stage":{"type":"testo_breve","risp":{}}},
        {"rispetto_orari":{"type":"scala_valutazione","risp":{}}},
        {"miglioramento_incarichi":{"type":"scala_valutazione","risp":{}}},
        {"lavoro_gruppo":{"type":"scala_valutazione","risp":{}}},
        {"empatia":{"type":"scala_valutazione","risp":{}}},
        {"accettazione_punti_vista":{"type":"scala_valutazione","risp":{}}}
    ])

    await form.insert_many([
        {"comunicazione_efficace":{"type":"scala_valutazione","risp":{}}},
        {"chiedere_aiuto":{"type":"scala_valutazione","risp":{}}},
        {"curiosita_motivazione":{"type":"scala_valutazione","risp":{}}},
        {"utilita_competenze":{"type":"scala_valutazione","risp":{}}},
        {"altre_cose_imparate":{"type":"testo_lungo","risp":{}}},
        {"crescita_comunicazione":{"type":"scala_valutazione","risp":{}}}
    ])

    await form.insert_many([
        {"imparato_stage":{"type":"scala_valutazione","risp":{},"possible_risp":["Problem solving","Empatia","Adattabilità","Autocontrollo","Lavoro di squadra/networking","Sicurezza in sé stessi","Spirito di collaborazione","Volontà di apprendere","Creatività e pensiero critico"]}},
        {"contesto_competenze": {"type": "scala_valutazione", "risp": {}, "possible_risp":["Nel mondo della scuola","Nel mondo del lavoro","Nell'attività di volontariato","Nel mio contesto di amici","In famiglia"]}},
        {"aspetti_volontariato": {"type": "scala_valutazione", "risp": {}, "possible_risp":["Conoscere nuove persone/realtà al di fuori della scuola","Impegnarsi in attività manuali","Scoprire nuovi interessi","Scoprire nuove capacità","Svolgere attività di tuo interesse","Lavorare in gruppo"]}},
        {"felicita_classe": {"type": "scala_valutazione", "risp": {}}},
        {"regole_scuola": {"type": "scala_valutazione", "risp": {}}},
        {"parte_gruppo": {"type": "scala_valutazione", "risp": {}}}
    ])

    await form.insert_many([
        {"soddisfazione_voti": {"type": "scala_valutazione", "risp": {}}},
        {"relazioni_classe": {"type": "scala_valutazione", "risp": {}}},
        {"conoscenza_bisogni": {"type": "scala_valutazione", "risp": {}}},
        {"supporto_famiglia": {"type": "scala_valutazione", "risp": {}}}
    ])
asyncio.run(make_up())
