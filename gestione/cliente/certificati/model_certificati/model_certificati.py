import os
import pickle

# cliente/
class Insieme_Certificati():
    def __init__(self):
        super(Insieme_Certificati, self).__init__()
        self.lista_certificati = []
        # print("ok")
        # k = os.path.isfile("gestione/clienti/certificati/data_certificati/lista_certificati_salvata.pickle")
        # print(k)
        if os.path.isfile("gestione/clienti/certificati/data_certificati/lista_certificati_salvata.pickle"):
            # print("ok2")
            with open("gestione/clienti/certificati/data_certificati/lista_certificati_salvata.pickle", "rb") as file:
                # print("file recuperato")
                self.lista_certificati = pickle.load(file)
                print("file recuperato2")

    def aggiungi_certificato(self, certificato):
        self.lista_certificati.append(certificato)

    def rimuovi_certificato_by_id(self, id):
        for certificato in self.lista_certificati:
            if certificato.id == id:
                self.lista_certificati.remove(certificato)
                return True
        return False

    def get_lista_certificati(self):
        return self.lista_certificati

    def get_certificato_by_id(self, id):
        for certificato in self.lista_certificati:
            if certificato.id == id:
                return certificato
        return None

    def save_data(self):
        if os.path.isfile("gestione/cliente/certificati/data_certificati/lista_certificati_salvata.pickle"):
            with open("gestione/cliente/certificati/data_certificati/lista_certificati_salvata.pickle", "wb") as handle:
                pickle.dump(self.lista_certificati, handle, pickle.HIGHEST_PROTOCOL)