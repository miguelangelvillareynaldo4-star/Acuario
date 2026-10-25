from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image as KivyImage
from plyer import filechooser

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0.08, 0.08, 0.08, 1
        MDTopAppBar:
            title: "AcuarioApp"
            md_bg_color: 0.08, 0.08, 0.08, 1
            elevation: 0
        ScrollView:
            MDBoxLayout:
                id: chat_box
                orientation: 'vertical'
                adaptive_height: True
                padding: dp(12)
                spacing: dp(16)
        MDBoxLayout:
            size_hint_y: None
            height: 90
            padding: 12
            MDCard:
                radius: 24
                md_bg_color: 0.18, 0.18, 0.18, 1
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTextField:
                        id: input_field
                        hint_text: "Responder..."
                        mode: "rectangle"
                        line_color_normal: 0,0,0,0
                        on_text_validate: app.send_message()
                    MDBoxLayout:
                        size_hint_y: None
                        height: 40
                        spacing: 4
                        MDIconButton:
                            icon: "plus"
                            on_release: app.pick_photo()
                        MDIconButton:
                            icon: "microphone"
                            on_release: app.voice_input()
                        Widget:
                        MDIconButton:
                            icon: "send"
                            on_release: app.send_message()
'''

class AcuarioApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(KV)
        self.add_ai("Hola! Soy tu asistente. Preguntame lo que quieras, en el idioma que quieras. Puedes escribirme, hablarme con el microfono o mandarme una foto.")
        return self.screen

    def add_user(self, text):
        row = MDBoxLayout(orientation='horizontal', size_hint_y=None, adaptive_height=True)
        row.add_widget(MDLabel(size_hint_x=0.2))
        card = MDCard(size_hint_x=0.8, radius=20, md_bg_color=(0.22,0.22,0.22,1), padding=12)
        lbl = MDLabel(text=text, size_hint_y=None)
        lbl.bind(texture_size=lambda *x: setattr(lbl, 'height', lbl.texture_size[1]))
        card.add_widget(lbl)
        card.height = lbl.height + 24
        row.add_widget(card); row.height = card.height
        self.screen.ids.chat_box.add_widget(row)

    def add_ai(self, text):
        lbl = MDLabel(text=text, size_hint_y=None, font_size=16)
        lbl.text_size = (self.screen.width - 40, None)
        lbl.bind(texture_size=lambda *x: setattr(lbl, 'height', lbl.texture_size[1]+10))
        self.screen.ids.chat_box.add_widget(lbl)

    def send_message(self):
        txt = self.screen.ids.input_field.text.strip()
        if not txt: return
        self.add_user(txt)
        self.screen.ids.input_field.text = ""
        low = txt.lower()
        if any(w in low for w in ["how","what","is","you","hello","hi"]):
            resp = f"Got it! You asked: '{txt}'. I'm here to help you with anything you need. Tell me more and I will answer you."
        elif any(w in low for w in ["como","que","hola","puedes","meu","voce"]):
            resp = f"Entendido! Me preguntaste: '{txt}'. Estoy aqui para ayudarte con lo que sea. Dime mas y te respondo."
        else:
            resp = f"Entendido! Me escribiste: '{txt}'. Te ayudo con eso, dime un poco mas para darte una respuesta completa."
        self.add_ai(resp)

    def voice_input(self):
        self.add_ai("Te estoy escuchando... habla ahora.")
        self.screen.ids.input_field.text = ""

    def pick_photo(self):
        filechooser.open_file(on_selection=self.photo_selected, filters=["*.jpg","*.png","*.jpeg"])

    def photo_selected(self, sel):
        if sel:
            self.add_user("Foto enviada")
            self.screen.ids.chat_box.add_widget(KivyImage(source=sel[0], size_hint_y=None, height=220))
            self.add_ai("Ya vi tu foto! Se ve bien. Que quieres que te diga de ella?")

if __name__ == "__main__":
    AcuarioApp().run()
