import requests
import threading

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image as KivyImage
from plyer import filechooser

Window.softinput_mode = 'below_target'

# PEGA AQUI TU DIRECCION WEB DE APPS SCRIPT
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbypM4Ajj3FlDiNjQuS_aisCjRagizkG-64qmbBRM5cqtbkgtjUtAgkA6gXjAWvXrjTnIQ/exec"


class ChatApp(App):

    def build(self):
        root = BoxLayout(
            orientation='vertical',
            padding=15,
            spacing=10
        )

        top = BoxLayout(
            size_hint_y=None,
            height=50,
            spacing=10
        )

        top.add_widget(Button(
            text="=",
            size_hint=(None, None),
            size=(45, 45)
        ))

        top.add_widget(Label(
            text="Acuario",
            bold=True,
            font_size=22
        ))

        top.add_widget(Button(
            text="O",
            size_hint=(None, None),
            size=(45, 45)
        ))

        root.add_widget(top)

        self.chat_box = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=15,
            padding=10
        )

        self.chat_box.bind(
            minimum_height=self.chat_box.setter('height')
        )

        scroll = ScrollView()
        scroll.add_widget(self.chat_box)
        root.add_widget(scroll)

        def opcion(icono, texto):
            fila = BoxLayout(
                size_hint_y=None,
                height=60,
                spacing=15
            )

            fila.add_widget(Button(
                text=icono,
                size_hint=(None, None),
                size=(55, 55)
            ))

            btn = Button(
                text=texto,
                halign='left',
                font_size=18,
                bold=True
            )

            btn.bind(
                on_release=lambda x: self.pregunta_sugerida(texto)
            )

            fila.add_widget(btn)
            return fila

        self.chat_box.add_widget(
            opcion("IMG", "Crie uma imagem")
        )

        self.chat_box.add_widget(
            opcion("?", "Explore o dia de hoje na historia")
        )

        self.chat_box.add_widget(
            opcion("O", "Encontre algo gratuito para fazer")
        )

        bottom_box = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=110,
            padding=10
        )

        self.input_field = TextInput(
            hint_text="Pergunte ao Acuario...",
            multiline=False,
            size_hint_y=None,
            height=50,
            font_size=18
        )

        self.input_field.bind(
            on_text_validate=lambda x: self.send_message()
        )

        bottom_box.add_widget(self.input_field)

        fila_botones = BoxLayout(
            size_hint_y=None,
            height=50,
            spacing=10
        )

        btn_plus = Button(
            text="+",
            size_hint=(None, None),
            size=(45, 45)
        )

        btn_plus.bind(
            on_release=lambda x: self.pick_photo()
        )

        fila_botones.add_widget(btn_plus)
        fila_botones.add_widget(Label(size_hint_x=1))

        btn_instant = Button(
            text="Instantaneo",
            size_hint=(None, None),
            size=(130, 45)
        )

        btn_mic = Button(
            text="MIC",
            size_hint=(None, None),
            size=(45, 45)
        )

        btn_mic.bind(
            on_release=lambda x: self.voice_input()
        )

        btn_send = Button(
            text=">",
            size_hint=(None, None),
            size=(45, 45),
            background_color=(0.2, 0.5, 1, 1)
        )

        btn_send.bind(
            on_release=lambda x: self.send_message()
        )

        fila_botones.add_widget(btn_instant)
        fila_botones.add_widget(btn_mic)
        fila_botones.add_widget(btn_send)

        bottom_box.add_widget(fila_botones)
        root.add_widget(bottom_box)

        return root

    def pregunta_sugerida(self, texto):
        self.add_user(texto)

        if "imagem" in texto.lower():
            self.add_ai(
                "Claro! Descreva a imagem que voce quer criar."
            )

        elif "historia" in texto.lower():
            self.add_ai(
                "Que periodo da historia voce quer conhecer?"
            )

        else:
            self.add_ai(
                "Diga sua cidade e o que voce gosta de fazer."
            )

    def add_user(self, texto):
        lbl = Label(
            text=texto,
            size_hint_y=None,
            halign='right',
            valign='middle'
        )

        lbl.bind(
            width=lambda obj, w: setattr(
                obj, 'text_size', (w, None)
            )
        )

        lbl.bind(
            texture_size=lambda obj, size: setattr(
                obj, 'height', size[1] + 15
            )
        )

        self.chat_box.add_widget(lbl)

    def add_ai(self, texto):
        lbl = Label(
            text=texto,
            size_hint_y=None,
            halign='left',
            valign='middle'
        )

        lbl.bind(
            width=lambda obj, w: setattr(
                obj, 'text_size', (w, None)
            )
        )

        lbl.bind(
            texture_size=lambda obj, size: setattr(
                obj, 'height', size[1] + 15
            )
        )

        self.chat_box.add_widget(lbl)

    def get_answer(self, txt):
        if not APPS_SCRIPT_URL.startswith("https://"):
            raise Exception("Falta configurar a URL")

        response = requests.post(
            APPS_SCRIPT_URL,
            json={"mensaje": txt},
            timeout=45
        )

        response.raise_for_status()
        data = response.json()

        if not data.get("ok"):
            raise Exception(
                data.get("error", "Erro ao consultar Gemini")
            )

        return data["respuesta"]

    def send_message(self):
        txt = self.input_field.text.strip()

        if not txt:
            return

        self.add_user(txt)
        self.input_field.text = ""

        self.add_ai("Acuario esta pensando...")

        threading.Thread(
            target=self._consultar_gemini,
            args=(txt,),
            daemon=True
        ).start()

    def _consultar_gemini(self, txt):
        try:
            respuesta = self.get_answer(txt)

            Clock.schedule_once(
                lambda dt: self.add_ai(respuesta),
                0
            )

        except Exception as e:
            print("Erro de conexao:", str(e))

            Clock.schedule_once(
                lambda dt: self.add_ai(
                    "Nao consegui conectar com Gemini. "
                    "Verifique a internet e a URL do Apps Script."
                ),
                0
            ) 

    def voice_input(self):
        self.add_ai(
            "O microfone ainda precisa ser configurado."
        )

    def pick_photo(self):
        try:
            filechooser.open_file(
                on_selection=self.photo_selected
            )

        except Exception:
            self.add_ai(
                "Nao consegui abrir as fotos. "
                "Verifique as permissoes do aplicativo."
            )

    def photo_selected(self, sel):
        if sel:
            self.add_user("Foto selecionada")

            self.chat_box.add_widget(
                KivyImage(
                    source=sel[0],
                    size_hint_y=None,
                    height=220
                )
            )

            self.add_ai(
                "A foto foi selecionada. "
                "A analise de imagens ainda precisa ser conectada."
            )


if __name__ == "__main__":
    ChatApp().run()
