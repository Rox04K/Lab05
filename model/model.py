from database.corso_DAO import DAO


class Model:
    def __init__(self):
        self._IDMapIscrizioni = set()
        self.loadID()

    def getCorsi(self):
        corsi = DAO.getAllCorsi()
        ordinato = sorted(corsi, key=lambda c:c.codins)
        return ordinato

    def getIscrittiCorso(self, codCorso):
        iscritti = DAO.getIscrittiCorso(codCorso)
        ordinato = sorted(iscritti, key=lambda s: s.matricola)
        return ordinato

    def getStudente(self, matricola):
        studente = DAO.getStudente(matricola)
        print(studente)
        return studente

    def getCorsiStudente(self, matricola):
        corsi = DAO.getCorsiStudente(matricola)
        ordinato = sorted(corsi, key=lambda c: c.codins)
        return ordinato

    def iscriviStudente(self, corso, matricola):
        tupla = (matricola, corso)
        if tupla in self._IDMapIscrizioni:
            return False

        DAO.iscriviStudente(corso, matricola)
        self._IDMapIscrizioni.add(tupla)
        return True

    def loadID(self):
        tuple = DAO.getAllIscrizioni()
        self._IDMapIscrizioni = {t for t in tuple}