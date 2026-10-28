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
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # ARRIBA IGUAL QUE TU FOTO
        top = BoxLayout(size_hint_y=None, height=50, spacing=10)
        top.add_widget(Button(text="=", size_hint=(None, None), size=(45, 45)))
        top.add_widget(Label(text="Acuario", bold=True, font_size=22, halign='left', size_hint_x=1))
        top.add_widget(Button(text="O", size_hint=(None, None), size=(45, 45)))
        root.add_widget(top)

        # MEDIO IGUAL QUE TU FOTO
        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=25, padding=10)
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        scroll = ScrollView()
        scroll.add_widget(self.chat_box)
        root.add_widget(scroll)

        # Las 3 opciones de tu foto
        def opcion(icono, texto):
            fila = BoxLayout(size_hint_y=None, height=60, spacing=15)
            fila.add_widget(Button(text=icono, size_hint=(None, None), size=(55, 55)))
            btn = Button(text=texto, halign='left', font_size=18, bold=True)
            btn.bind(on_release=lambda x: self.pregunta_sugerida(texto))
            fila.add_widget(btn)
            return fila

        self.chat_box.add_widget(opcion("IMG", "Crie uma imagem"))
        self.chat_box.add_widget(opcion("?", "Explore o dia de hoje na historia"))
        self.chat_box.add_widget(opcion("O", "Encontre algo gratuito para fazer"))

        # ABAJO IGUAL QUE TU FOTO - CUADRO GRIS REDONDO GRANDE
        bottom_box = BoxLayout(orientation='vertical', size_hint_y=None, height=110, padding=10)
        self.input_field = TextInput(hint_text="Pergunte a Meta AI...", multiline=False, size_hint_y=None, height=50, font_size=18)
        self.input_field.bind(on_text_validate=lambda x: self.send_message())
        bottom_box.add_widget(self.input_field)

        fila_botones = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_plus = Button(text="+", size_hint=(None, None), size=(45, 45))
        btn_plus.bind(on_release=lambda x: self.pick_photo())
        # Espacio para centrar
        fila_botones.add_widget(btn_plus)
        fila_botones.add_widget(Label(size_hint_x=1))
        btn_instant = Button(text="Instantaneo", size_hint=(None, None), size=(130, 45))
        # MIC CON LOGO, no letras
        btn_mic = Button(size_hint=(None, None), size=(45, 45), background_normal='mic.png', background_down='mic.png', text='')
        btn_mic.bind(on_release=lambda x: self.voice_input())
        btn_send = Button(text=">", size_hint=(None, None), size=(45, 45), background_color=(0.2, 0.5, 1, 1))
        btn_send.bind(on_release=lambda x: self.send_message())
        fila_botones.add_widget(btn_instant)
        fila_botones.add_widget(btn_mic)
        fila_botones.add_widget(btn_send)
        bottom_box.add_widget(fila_botones)
        root.add_widget(bottom_box)
        return root

    def pregunta_sugerida(self, texto):
        self.add_user(texto)
        if "imagem" in texto.lower():
            self.add_ai("Claro! Que imagen quieres que cree? Dime como la quieres y te la hago.")
        elif "historia" in texto.lower():
            self.add_ai("Hoy en la historia pasaron muchas cosas interesantes. Dime que dia te interesa y te cuento.")
        else:
            self.add_ai("Te busco algo gratuito para hacer cerca de ti. Dime en que ciudad estas y que te gusta hacer.")

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
        if "hola" in t: return "Hola mi hermano! Que bueno verte por aqui. Dime que quieres saber hoy?"
        if "que puedes" in t: return "Puedo crear imagenes, contarte la historia de hoy y buscarte cosas gratis para hacer, igual que en la foto que me mandaste."
        return "Buena pregunta. Me preguntaste: '" + txt + "'. Cuentame un poco mas y te respondo completo, como Acuario."

    def send_message(self):
        txt = self.input_field.text.strip()
        if not txt: return
        self.add_user(txt)
        self.input_field.text = ""
        self.add_ai(self.get_answer(txt))

    def voice_input(self):
        self.add_ai("Te estoy escuchando, habla ahora.")

    def pick_photo(self):
        try:
            filechooser.open_file(on_selection=self.photo_selected)
        except:
            self.add_ai("Dale permiso en Ajustes > Fotos y Archivos para que suba la foto.")

    def photo_selected(self, sel):
        if sel:
            self.add_user("Foto enviada")
            self.chat_box.add_widget(KivyImage(source=sel[0], size_hint_y=None, height=220))
            self.add_ai("Ya vi tu foto! Dime que quieres que te diga de ella.")

if __name__ == "__main__":
    ChatApp().run()
