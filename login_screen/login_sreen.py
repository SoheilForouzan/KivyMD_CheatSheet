from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" # Makes the overall app theme Dark(default = Light)
        self.theme_cls.primary_palette = "BlueGray" # To set the primary pallet color
        return Builder.load_file('login_screen.kv')
    
    def logger(self):
        self.root.ids.welcome_label.text = f'sup {self.root.ids.user.text}!'

    def clear(self):
        self.root.ids.welcome_label.text = 'welcome'
        self.root.ids.user.text = ''
        self.root.ids.passwd.text = ''
        
MainApp().run()