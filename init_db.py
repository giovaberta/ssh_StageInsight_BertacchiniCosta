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
        {"dati_ets":{"type":"testo_breve","risp":{}},"testo_domanda":"Dati dell'ETS:"},
        {"dati_alunno":{"type":"testo_breve","risp":{}}, "testo_domanda":"Dati dell'alunn*:"},
        {"percorso_studente":{"type":"testo_breve","risp":{}},"testo_domanda": "Se sei uno studente specifica il tuo percorso:"},
        {"prima_esperienza":{"type":"si_no","risp":{}},"testo_domanda":"È la prima esperienza di volontariato e cittadinanza?"},
        {"fonte_info":{"type":"menu_tendina","risp":{},"possible_risp":["Progetto Cantieri Giovani","Dalla scuola","Dall'informagiovani","Dai centri giovani","Dal CSV Terre Estensi","Materiale promozionale","Servizi sociali","Dalla mia famiglia","Da un amico"]},"testo_domanda":"Dove o da chi hai ricevuto le informazioni per poter fare questa esperienza?"},
        {"motivazioni":{"type":"scelta_multipla","risp":{},"possible_risp":["Il confronto con i miei insegnanti","Gli stimoli degli amici","Gli stimoli della mia famiglia","La curiosità di provare qualcosa di nuovo","Le mie convinzioni personali","Qualche cosa che mi è successo"]},"testo_domanda":"Quali sono le motivazioni personali che ti hanno spinto a fare questa esperienza?"}
    ])

    await form.insert_many([
        {"ruolo_stage":{"type":"testo_breve","risp":{}},"testo_domanda":"Che ruolo hai avuto durante lo stage?"},
        {"rispetto_orari":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Credi di essere riuscit* a rispettare orari, appuntamenti, impegni e scadenze?"},
        {"miglioramento_incarichi":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Ritieni di essere migliorat* nella tua capacità di portare a termine gli incarichi assegnati?"},
        {"lavoro_gruppo":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Quanto sei riuscit* a lavorare in gruppo?"},
        {"empatia":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Quanto sei riuscit* a comprendere gli stati d'animo e le emozioni altrui (empatia)?"},
        {"accettazione_punti_vista":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Quanto sei riuscit* ad ascoltare ed accettare i punti di vista diversi dai tuoi?"}
    ])

    await form.insert_many([
        {"comunicazione_efficace":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Sei riuscit* a comunicare in modo efficace?"},
        {"chiedere_aiuto":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Sei riuscit* a chiedere aiuto quando non sapevi fare qualcosa?"},
        {"curiosita_motivazione":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Quanto questa esperienza ti ha incuriosit* e motivat*?"},
        {"utilita_competenze":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Le tue competenze (relazionali, informatiche, linguistiche, ecc) ti sono state utili in questa esperienza?"},
        {"altre_cose_imparate":{"type":"testo_lungo","risp":{}},"testo_domanda":"Ci sono altre cose che hai imparato/sviluppato non elencate sopra che vuoi dirci?"},
        {"crescita_comunicazione":{"type":"scala_valutazione","risp":{}},"testo_domanda":"Quanto è cresciuta la tua capacità di comunicare in modo efficace?"}
    ])

    await form.insert_many([
        {"imparato_stage":{"type":"scala_valutazione","risp":{},"possible_risp":["Problem solving","Empatia","Adattabilità","Autocontrollo","Lavoro di squadra/networking","Sicurezza in sé stessi","Spirito di collaborazione","Volontà di apprendere","Creatività e pensiero critico"]},"testo_domanda":"Cosa pensi di aver imparato dall’esperienza di stage?"},
        {"contesto_competenze": {"type": "scala_valutazione", "risp": {}, "possible_risp":["Nel mondo della scuola","Nel mondo del lavoro","Nell'attività di volontariato","Nel mio contesto di amici","In famiglia"]},"testo_domanda":"In quale contesto pensi che potresti spendere le competenze che hai sviluppato?"},
        {"aspetti_volontariato": {"type": "scala_valutazione", "risp": {}, "possible_risp":["Conoscere nuove persone/realtà al di fuori della scuola","Impegnarsi in attività manuali","Scoprire nuovi interessi","Scoprire nuove capacità","Svolgere attività di tuo interesse","Lavorare in gruppo"]},"testo_domanda":"Quanto reputi interessanti i seguenti aspetti dell'attività di volontariato?"},
        {"felicita_classe": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto sei soddisfatto/a dei seguenti aspetti della tua vita scolastica e personale? (Moltissimo, Molto, Abbastanza, Poco per nulla)"},
        {"regole_scuola": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto pensi che le regole della scuola siano importanti e giuste?"},
        {"parte_gruppo": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto ti senti parte di un gruppo di amici e compagni di classe?"}
    ])

    await form.insert_many([
        {"soddisfazione_voti": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto sei soddisfatto dei tuoi voti?"},
        {"relazioni_classe": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto riesci a relazionarti con gli altri in classe e a lavorare in gruppo?"},
        {"conoscenza_bisogni": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto pensi di conoscere i tuoi bisogni e desideri?"},
        {"supporto_famiglia": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Quanto ti senti supportato dalla tua famiglia?"},
        {"gestione_imprevisti": {"type": "scala_valutazione", "risp": {}},"testo_domanda":"Sei riuscit* ad affrontare e gestire gli imprevisti?"}
    ])
asyncio.run(make_up())
