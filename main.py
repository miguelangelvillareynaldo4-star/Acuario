from kivy.app import App
from kivy.core.window import Window
Window.softinput_mode = 'below_target'
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image as KivyImage
from plyer import filechooser

class ChatApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        top = BoxLayout(size_hint_y=None, height=50)
        top.add_widget(Label(text="AcuarioApp", bold=True, font_size=20))
        root.add_widget(top)

        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=10)
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        scroll = ScrollView()
        scroll.add_widget(self.chat_box)
        root.add_widget(scroll)
        self.add_ai("Hola! Soy tu asistente. Preguntame lo que quieras.")

        # ABAJO COMO TU ME DIJISTE
        bottom = BoxLayout(size_hint_y=None, height=70, padding=8, spacing=8)
        btn_plus = Button(text="+", size_hint=(None, None), size=(50, 50))
        btn_plus.bind(on_release=lambda x: self.pick_photo())
        btn_mic = Button(text="MIC", size_hint=(None, None), size=(50, 50))
        btn_mic.bind(on_release=lambda x: self.voice_input())
        self.input_field = TextInput(hint_text="Responder...", multiline=False, size_hint_y=None, height=50, font_size=18)
        self.input_field.bind(on_text_validate=lambda x: self.send_message())
        btn_send = Button(text=">", size_hint=(None, None), size=(50, 50))
        btn_send.bind(on_release=lambda x: self.send_message())
        bottom.add_widget(btn_plus)
        bottom.add_widget(btn_mic)
        bottom.add_widget(self.input_field)
        bottom.add_widget(btn_send)
        root.add_widget(bottom)
        return root

    def add_user(self, text):
        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        row.add_widget(Label(size_hint_x=0.3))
        row.add_widget(Label(text=text, size_hint_x=0.7))
        self.chat_box.add_widget(row)

    def add_ai(self, text):
        lbl = Label(text=text, size_hint_y=None, text_size=(350, None), halign='left')
        lbl.bind(texture_size=lambda *x: setattr(lbl, 'height', lbl.texture_size[1]+10))
        self.chat_box.add_widget(lbl)

    def get_answer(self, txt):
        t = txt.lower()
        if "hola" in t or "que puedes" in t:
            return "Hola! Puedo ayudarte con lo que sea, preguntame y te respondo."
        if "como estas" in t:
            return "Estoy bien, y tu?"
        if "gracias" in t:
            return "De nada!"
        return "Te entendi: " + txt + ". Dime un poco mas para ayudarte mejor."

    def send_message(self):
        txt = self.input_field.text.strip()
        if not txt: return
        self.add_user(txt)
        self.input_field.text = ""
        self.add_ai(self.get_answer(txt))

    def voice_input(self):
        self.add_ai("Te escucho...")

    def pick_photo(self):
        try:
            filechooser.open_file(on_selection=self.photo_selected)
        except:
            self.add_ai("Dale permiso en Ajustes > Fotos.")

    def photo_selected(self, sel):
        if sel:
            self.add_user("Foto enviada")
            self.chat_box.add_widget(KivyImage(source=sel[0], size_hint_y=None, height=220))
            self.add_ai("Ya vi tu foto!")

if __name__ == "__main__":
    ChatApp().run()
