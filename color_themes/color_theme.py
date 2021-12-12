from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" # Makes the overall app theme Dark(default = Light)
        self.theme_cls.primary_palette = "Blue" # To set the primary pallet color
        self.theme_cls.accent_palette = "Red" # To set the primary accent color
        return Builder.load_file('color_theme.kv')

MainApp().run()