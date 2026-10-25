from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import os

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "AcuarioApp"
            left_action_items: [["fish", lambda x: None]]
            right_action_items: [["plus", lambda x: app.open_add_dialog()]]
            md_bg_color: 0, 0.6, 0.55, 1

        MDBoxLayout:
            orientation: 'vertical'
            padding: 16
            spacing: 12

            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: 130
                padding: 16
                md_bg_color: 0.18, 0.18, 0.18, 1
                MDLabel:
                    text: "Aquarium overview"
                    font_style: "H5"
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                MDLabel:
                    text: "All systems stable"
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                MDLabel:
                    id: count_label
                    text: "3 tanks monitored"
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1

            ScrollView:
                MDList:
                    id: tank_list

            MDBoxLayout:
                size_hint_y: None
                height: 60
                spacing: 12
                MDRaisedButton:
                    text: "FOTO"
                    icon: "camera"
                    md_bg_color: 0, 0.6, 0.55, 1
                    on_release: app.pick_photo()
                MDRaisedButton:
                    text: "NUEVO TANQUE"
                    icon: "plus"
                    md_bg_color: 0, 0.6, 0.55, 1
                    on_release: app.open_add_dialog()

            MDLabel:
                id: photo_label
                text: "No photo selected"
                halign: "center"
                size_hint_y: None
                height: 30

            Image:
                id: photo_img
                source: ""
                allow_stretch: True
                keep_ratio: True
'''

from kivymd.uix.list import MDList, OneLineListItem

class AcuarioApp(MDApp):
    dialog = None
    tanks = ListProperty([])

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.store = JsonStore(os.path.join(self.user_data_dir, 'tanks.json'))
        if self.store.exists('tanks'):
            self.tanks = self.store.get('tanks')['list']
        else:
            self.tanks = [
                "Main Reef - Coral and reef fish | 220L",
                "Nursery Tank - Shrimp and juveniles | 90L",
                "Quarantine - Empty | 50L",
            ]
            self.save_tanks()
        self.screen = Builder.load_string(KV)
        self.refresh_list()
        return self.screen

    def save_tanks(self):
        self.store.put('tanks', list=self.tanks)

    def refresh_list(self):
        lst = self.screen.ids.tank_list
        lst.clear_widgets()
        self.screen.ids.count_label.text = f"{len(self.tanks)} tanks monitored"
        for t in self.tanks:
            item = OneLineListItem(text=t)
            item.bind(on_release=lambda x, txt=t: self.show_detail(txt))
            lst.add_widget(item)

    def show_detail(self, txt):
        d = MDDialog(
            title=txt,
            text="Tanque seleccionado. Aqui puedes ver temperatura, pH y proximo cambio de agua.",
            buttons=[MDFlatButton(text="CERRAR", on_release=lambda x: d.dismiss())]
        )
        d.open()

    def open_add_dialog(self):
        self.name_field = MDTextField(hint_text="Nombre del tanque - ej: Betta Tank")
        self.info_field = MDTextField(hint_text="Descripcion | Litros - ej: Betta | 20L")
        content = MDBoxLayout(orientation="vertical", spacing=10, size_hint_y=None, height=110)
        content.add_widget(self.name_field)
        content.add_widget(self.info_field)
        self.dialog = MDDialog(
            title="Nuevo tanque",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(text="CANCELAR", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="GUARDAR", on_release=self.add_tank)
            ]
        )
        self.dialog.open()

    def add_tank(self, *args):
        name = self.name_field.text.strip()
        info = self.info_field.text.strip()
        if name:
            full = f"{name} - {info}" if info else name
            self.tanks.append(full)
            self.save_tanks()
            self.refresh_list()
        self.dialog.dismiss()

    def pick_photo(self):
        try:
            from plyer import filechooser
            filechooser.open_file(on_selection=self.on_photo_selected, filters=["*.png", "*.jpg", "*.jpeg"])
        except Exception as e:
            self.screen.ids.photo_label.text = f"Error: {e}"

    def on_photo_selected(self, selection):
        if selection:
            path = selection[0]
            self.screen.ids.photo_img.source = path
            self.screen.ids.photo_label.text = "Foto cargada: " + os.path.basename(path)
            self.screen.ids.photo_img.reload()

if __name__ == "__main__":
    AcuarioApp().run()
