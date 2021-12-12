from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Dark"
        # To set the primary pallet color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('bar.kv')

    def presser(self):
        self.root.ids.my_label.text = "Button Pressed"


MainApp().run()
