import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorso = None
        self.btnIscritti = None
        self.txtMatricola = None
        self.txtNome = None
        self.txtCognome = None
        self.btnStudente = None
        self.btnCorsi = None
        self.btnIscrivi = None
        self.lvResult = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1 --> Elenco corsi e bottone Cerca Iscritti
        self.ddCorso = ft.Dropdown(label="Corso", width=800)
        self._controller.fillDDCorso()
        self.btnIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_cercaIscritti)
        row1 = ft.Row([self.ddCorso, self.btnIscritti],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW2 --> Matricola, Nome e Cognome
        self.txtMatricola = ft.TextField(hint_text="Matricola", width=200)
        self.txtNome = ft.TextField(hint_text="Nome", width=400, read_only=True)
        self.txtCognome = ft.TextField(hint_text="Cognome", width=400, read_only=True)
        row2 = ft.Row([self.txtMatricola, self.txtNome, self.txtCognome],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW3 --> Pulsanti Cerca studene, corsi, iscrivi
        self.btnStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_cercaStudenti)
        self.btnCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handle_cercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrizione)
        row3 = ft.Row([self.btnStudente, self.btnCorsi, self.btnIscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.lvResult = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lvResult)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
