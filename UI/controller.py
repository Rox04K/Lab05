import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._corsoScelto = None

    def fillDDCorso(self):
        corsi = self._model.getCorsi()

        for c in corsi:
            self._view.ddCorso.options.append(ft.dropdown.Option(
                key = c.codins,
                text = c.__str__(),
                data = c,
                on_click = self._read_choice
            ))

        self._view.update_page()

    def _read_choice(self,e):
        self._corsoScelto = e.control.data

    def handle_cercaIscritti(self,e):

        corso = self._corsoScelto
        if corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        iscritti = self._model.getIscrittiCorso(corso.codins)

        self._view.lvResult.controls.append(ft.Text(f'Ci sono {len(iscritti)} al corso'))
        for i in iscritti:
            self._view.lvResult.controls.append(ft.Text(f'{i}'))

        self._view.update_page()

    def handle_cercaStudenti(self,e):

        self._view.lvResult.controls.clear()

        matricolaIn = self._view.txtMatricola.value
        if matricolaIn is None or matricolaIn == "":
            self._view.create_alert("Inserire la matricola!")
            return

        if not matricolaIn.isdigit():
            self._view.create_alert("La matricola deve essere un numero!")
            return

        matricola = int(matricolaIn)

        studente = self._model.getStudente(matricola)
        print(studente)
        if not studente:
            self._view.lvResult.controls.append(ft.Text("Studente non trovato", color="red"))
            self._view.update_page()
            return

        self._view.lvResult.controls.append(ft.Text('Studente correttamente trovato, '
                                                    'è possibile visualizzare i valori all\'interno '
                                                    'dell\'apposito spazio', color="green"))

        trovato = studente[0]
        self._view.txtNome.value = trovato.nome.upper()
        self._view.txtCognome.value = trovato.cognome.upper()

        self._view.update_page()

    def handle_cercaCorsi(self,e):
        self._view.lvResult.controls.clear()

        matricolaIn = self._view.txtMatricola.value
        if matricolaIn is None or matricolaIn == "":
            self._view.create_alert("Inserire la matricola!")
            return

        if not matricolaIn.isdigit():
            self._view.create_alert("La matricola deve essere un numero!")
            return

        matricola = int(matricolaIn)
        studente = self._cercaStudente(matricola)

        if not studente:
            return

        corsi = self._model.getCorsiStudente(matricola)
        if not corsi:
            self._view.lvResult.controls.append(ft.Text("Nessun corso per lo studente indicato", color="red"))
            self._view.update_page()
            return

        self._view.lvResult.controls.append(ft.Text(f'Risultano {len(corsi)} corsi'))
        for c in corsi:
            self._view.lvResult.controls.append(ft.Text(f'{c}'))

        self._view.update_page()

    def handle_iscrizione(self,e):
        self._view.lvResult.controls.clear()

        corso = self._corsoScelto
        if corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        matricolaIn = self._view.txtMatricola.value
        if matricolaIn is None or matricolaIn == "":
            self._view.create_alert("Inserire la matricola!")
            return

        if not matricolaIn.isdigit():
            self._view.create_alert("La matricola deve essere un numero!")
            return

        matricola = int(matricolaIn)
        studente = self._cercaStudente(matricola)

        if not studente:
            self._view.create_alert("Indicare uno studente già nel database!")
            return

        successo = self._model.iscriviStudente(corso.codins, matricola)
        if not successo:
            self._view.create_alert('Studente già iscritto a quel corso!')
            return
        self._view.lvResult.controls.append(ft.Text('Iscrizione effettuata correttamente', color='green'))
        self._view.update_page()

    def _cercaStudente(self, matricola):
        studente = self._model.getStudente(matricola)
        if not studente:
            self._view.lvResult.controls.append(ft.Text("Studente non trovato", color="red"))
            self._view.update_page()
            return False

        self._view.lvResult.controls.append(ft.Text('Studente correttamente trovato, '
                                                    'è possibile visualizzare i valori all\'interno '
                                                    'dell\'apposito spazio', color="green"))

        trovato = studente[0]
        self._view.txtNome.value = trovato.nome.upper()
        self._view.txtCognome.value = trovato.cognome.upper()
        self._view.update_page()
        return True