from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.05, 0.05, 0.08, 1

        MDTopAppBar:
            title: "AcuarioApp"
            left_action_items: [["menu"]]
            right_action_items: [["pencil"]]
            elevation: 0

        ScrollView:
            MDList:
                id: chat_list
                padding: 10
                spacing: 5

        MDBoxLayout:
            size_hint_y: None
            height: 60
            padding: 8
            spacing: 8
            md_bg_color: 0.1, 0.1, 0.14, 1

            MDIconButton:
                icon: "plus"
                on_release: app.pick_photo()

            MDTextField:
                id: input_field
                hint_text: "Responder..."
                mode: "round"
                on_text_validate: app.send_message()

            MDIconButton:
                icon: "send"
                theme_text_color: "Custom"
                text_color: 0, 0.5, 1, 1
                on_release: app.send_message()
'''

class AcuarioApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.screen = Builder.load_string(KV)
        # Mensaje de bienvenida
        self.screen.ids.chat_list.add_widget(OneLineListItem(text="AcuarioApp: Hola! Preguntame lo que quieras de tu acuario."))
        return self.screen

    def send_message(self):
        txt = self.screen.ids.input_field.text.strip()
        if not txt:
            return
        self.screen.ids.chat_list.add_widget(OneLineListItem(text="Tu: " + txt))
        self.screen.ids.input_field.text = ""
        lower = txt.lower()

        # Detecta idioma y responde en el mismo
        if any(w in lower for w in ["how", "what", "tank", "fish", "water"]):
            if "tank" in lower or "fish" in lower:
                resp = "AcuarioApp: You have 3 tanks. Main Reef 220L is stable."
            else:
                resp = "AcuarioApp: Got it! I saved it."
        elif any(w in lower for w in ["como", "meu", "tanque", "peixe", "agua"]):
            if "tanque" in lower or "peixe" in lower:
                resp = "AcuarioApp: Voce tem 3 tanques. Main Reef 220L esta estavel."
            else:
                resp = "AcuarioApp: Entendido! Salvei."
        else:
            if "tanque" in lower:
                resp = "AcuarioApp: Tienes 3 tanques. Main Reef 220L esta estable."
            elif "foto" in lower:
                resp = "AcuarioApp: Toca el + para mandar una foto."
            else:
                resp = "AcuarioApp: Entendido! Lo anoto en tus tareas."
        self.screen.ids.chat_list.add_widget(OneLineListItem(text=resp))

    def pick_photo(self):
        self.screen.ids.chat_list.add_widget(OneLineListItem(text="Foto enviada: puedes elegir una foto de tu galeria"))

if __name__ == "__main__":
    AcuarioApp().run()
