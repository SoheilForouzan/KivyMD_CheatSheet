from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

    data = {
        # <"Title": "MDIcon"> visit https://materialdesignicons.com/ for more Material Design Icons

        "Python": "language-python",
        "C++": "language-cpp",
        "ruby": "language-ruby",
    }

    def callback(self, instance):
        self.root.ids.my_label.text = f"{instance.icon} was pressed"

    def opened(self):
        self.root.ids.my_label.text = "Speed Dial was opened"

    def closed(self):
        self.root.ids.my_label.text = "Speed Dial was closed"
    def build(self):
        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"  # To set the primary pallet color
        # To set the primary accent color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        return Builder.load_file('speed_dial.kv')


MainApp().run()
