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
            left_action_items: [["menu"]]
            right_action_items: [["pencil", lambda x: app.new_chat()]]
            elevation: 0
            md_bg_color: 0.08, 0.08, 0.08, 1

        ScrollView:
            id: scroll
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
                padding: 8
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
                            theme_text_color: "Custom"
                            text_color: 0.2, 0.6, 1, 1
                            on_release: app.send_message()
'''

class AcuarioApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(KV)
        self.add_ai("Hola! Escribeme o hablame con el microfono, te respondo en tu idioma.")
        return self.screen

    def add_user(self, text):
        row = MDBoxLayout(orientation='horizontal', size_hint_y=None, adaptive_height=True)
        row.add_widget(MDLabel(size_hint_x=0.2))
        card = MDCard(size_hint_x=0.8, radius=20, md_bg_color=(0.22,0.22,0.22,1), padding=12)
        lbl = MDLabel(text=text, size_hint_y=None, theme_text_color="Primary")
        lbl.bind(texture_size=lambda *x: setattr(lbl, 'height', lbl.texture_size[1]))
        card.add_widget(lbl)
        card.height = lbl.height + 24
        row.add_widget(card)
        row.height = card.height
        self.screen.ids.chat_box.add_widget(row)

    def add_ai(self, text):
        lbl = MDLabel(text=text, size_hint_y=None, theme_text_color="Primary", font_size=16)
        lbl.text_size = (self.screen.width - 40, None)
        lbl.bind(texture_size=lambda *x: setattr(lbl, 'height', lbl.texture_size[1]+10))
        self.screen.ids.chat_box.add_widget(lbl)

    def new_chat(self):
        self.screen.ids.chat_box.clear_widgets()
        self.add_ai("Nuevo chat listo!")

    def send_message(self):
        txt = self.screen.ids.input_field.text.strip()
        if not txt: return
        self.add_user(txt)
        self.screen.ids.input_field.text = ""
        low = txt.lower()
        if any(w in low for w in ["how","what","tank","fish","water"]):
            resp = "You have 3 tanks. Main Reef 220L is stable, pH 7.2 and temp 26C."
        elif any(w in low for w in ["meu","tanque","peixe","agua"]):
            resp = "Voce tem 3 tanques. Main Reef 220L esta estavel, pH 7.2."
        else:
            if "tanque" in low or "peces" in low:
                resp = "Tienes 3 tanques. Main Reef de 220L esta estable, pH 7.2, temp 26C."
            else:
                resp = "Entendido! Lo anote para tu acuario."
        self.add_ai(resp)

    def voice_input(self):
        # Esto abre el dictado de voz de Android
        try:
            from android.speech import SpeechRecognizer
            from jnius import autoclass
            Intent = autoclass('android.content.Intent')
            RecognizerIntent = autoclass('android.speech.RecognizerIntent')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            activity.startActivityForResult(intent, 1234)
            self.add_ai("Te estoy escuchando... habla ahora.")
        except Exception:
            self.add_ai("Toca el microfono y habla, estoy escuchando. Si no abre, dale permiso de microfono en Ajustes.")
            # Si no hay voz, pone un ejemplo
            self.screen.ids.input_field.text = "como esta mi tanque?"

    def pick_photo(self):
        filechooser.open_file(on_selection=self.photo_selected, filters=["*.jpg","*.png","*.jpeg"])

    def photo_selected(self, sel):
        if sel:
            self.add_user("Foto de mi tanque")
            img = KivyImage(source=sel[0], size_hint_y=None, height=220)
            self.screen.ids.chat_box.add_widget(img)
            self.add_ai("Ya vi tu foto! El agua se ve clara y los peces bien.")

if __name__ == "__main__":
    AcuarioApp().run()
