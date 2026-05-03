# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllCorsi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select * from corso """

        cursor.execute(query)

        for row in cursor:
            result.append(Corso(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getIscrittiCorso(codCorso):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select s.matricola, s.cognome, s.nome, s.CDS from studente s , iscrizione i where i.matricola = s.matricola and i.codins=%s"""

        cursor.execute(query, (codCorso,))

        for row in cursor:
            result.append(Studente(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStudente(matricola):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select * from studente where matricola=%s"""

        cursor.execute(query, (matricola,))

        for row in cursor:
            result.append(Studente(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCorsiStudente(matricola):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select c.codins, c.crediti, c.nome, c.pd from corso c, iscrizione i where c.codins = i.codins and i.matricola = %s"""

        cursor.execute(query, (matricola,))

        for row in cursor:
            result.append(Corso(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def iscriviStudente(corso, matricola):
        conn = DBConnect.get_connection()


        cursor = conn.cursor(dictionary=True)
        query = """ INSERT INTO iscrizione (matricola, codins) VALUES (%s, %s)"""

        cursor.execute(query, (matricola, corso))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def getAllIscrizioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select * from iscrizione"""

        cursor.execute(query,)

        for row in cursor:
            result.append((row['matricola'], row['codins']))

        cursor.close()
        conn.close()
        return result