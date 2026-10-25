from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'

        # ARRIBA - como Meta AI
        MDTopAppBar:
            title: "AcuarioApp"
            left_action_items: [["menu", lambda x: app.open_menu()]]
            right_action_items: [["square-edit-outline", lambda x: app.new_chat()], ["dots-vertical", lambda x: app.open_menu()]]
            md_bg_color: 0,0,0,1
            specific_text_color: 1,1,1,1

        ScrollView:
            MDList:
                id: chat_list
                padding: 16
                spacing: 10

        # ABAJO - donde se escribe, como tu foto
        MDCard:
            orientation: 'horizontal'
            size_hint_y: None
            height: 65
            radius: [30,30,30,30]
            md_bg_color: 0.15,0.15,0.15,1
            padding: [12,8,12,8]
            spacing: 8
            pos_hint: {"center_x": .5}
            MDIconButton:
                icon: "plus"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
                on_release: app.pick_photo()
            MDTextField:
                id: input_field
                hint_text: "Responder..."
                mode: "fill"
                fill_color_normal: 0,0,0,0
                fill_color_focus: 0,0,0,0
                line_color_normal: 0,0,0,0
                line_color_focus: 0,0,0,0
                text_color_normal: 1,1,1,1
                on_text_validate: app.send_message()
            MDIconButton:
                icon: "microphone"
                theme_icon_color: "Custom"
                icon_color: 1,1,1,1
            MDIconButton:
                icon: "send"
                theme_icon_color: "Custom"
                icon_color: 0,0.6,1,1
                on_release: app.send_message()
'''

class AcuarioApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(KV)
        self.add_msg("Hola! Soy tu asistente de acuario 🐠 ¿Qué tanque quieres revisar?")
        return self.screen

    def add_msg(self, text):
        item = OneLineListItem(text=text)
        self.screen.ids.chat_list.add_widget(item)

    def send_message(self):
        txt = self.screen.ids.input_field.text.strip()
        if txt == "":
            return
        self.add_msg("Tu: " + txt)
        self.screen.ids.input_field.text = ""
        # respuesta automatica simple
        if "tanque" in txt.lower():
            self.add_msg("AcuarioApp: Tienes 3 tanques. Main Reef 220L esta estable.")
        elif "foto" in txt.lower():
            self.add_msg("AcuarioApp: Toca el + para mandar una foto.")
        else:
            self.add_msg("AcuarioApp: Entendido! Lo anoto en tus tareas.")

    def new_chat(self):
        self.screen.ids.chat_list.clear_widgets()
        self.add_msg("Nuevo chat creado. ¿Qué quieres preguntar de tu acuario?")

    def open_menu(self):
        d = MDDialog(title="Chats anteriores", text="Main Reef - Ayer\\nNursery Tank - Hace 2 dias\\nQuarantine - Semana pasada", buttons=[MDFlatButton(text="CERRAR", on_release=lambda x: d.dismiss())])
        d.open()

    def pick_photo(self):
        from kivymd.uix.filemanager import MDFileManager
        self.manager = MDFileManager(exit_manager=lambda x: self.manager.close(), select_path=self.on_photo)
        self.manager.show("/storage/emulated/0/DCIM")

    def on_photo(self, path):
        self.manager.close()
        self.add_msg("Foto enviada: " + path.split("/")[-1])

if __name__ == "__main__":
    AcuarioApp().run()
