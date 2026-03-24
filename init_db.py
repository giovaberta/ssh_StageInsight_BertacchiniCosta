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

    #Request
    keys = ['dati_ets', 'dati_alunno', 'percorso_studente', 'prima_esperienza', 'fonte_info', 'motivazioni', 'ruolo_stage', 'rispetto_orari', 'miglioramento_incarichi', 'lavoro_gruppo', 'empatia', 'accettazione_punti_vista', 'comunicazione_efficace', 'gestione_imprevisti', 'chiedere_aiuto', 'curiosita_motivazione', 'utilita_competenze', 'altre_cose_imparate', 'crescita_comunicazione', 'imparato_stage', 'contesto_competenze', 'aspetti_volontariato', 'felicita_classe', 'regole_scuola', 'parte_gruppo', 'soddisfazione_voti', 'relazioni_classe', 'conoscenza_bisogni', 'supporto_famiglia']
    for key in keys:
        await form.insert_one({key:{}})
asyncio.run(make_up())