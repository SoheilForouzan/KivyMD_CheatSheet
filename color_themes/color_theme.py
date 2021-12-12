from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"  # To set the primary pallet color
        # To set the primary accent color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('color_theme.kv')


MainApp().run()
