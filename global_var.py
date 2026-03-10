from pymongo import AsyncMongoClient

"""
File che conntiene le variabili globali utili per l'intera applicazione
"""

Client = AsyncMongoClient("localhost", 27017)
db = Client["SSH"] # DataBase
user = db["user"] # Collezzione dove si trovano le informazioni sugli utenti
# Es: {"name":NomeUtente,"pw":password,"type":0/1/2/3} 0.Proprietario della rete 1.Admin 2.Studente/operatore 3.Guest
form = db["form"] # Collezione dove si trovano le risposte ai vari form con relativo collegamento all'utente (Se ancora esistente)