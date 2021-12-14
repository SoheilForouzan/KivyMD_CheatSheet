# We didn't use .kv file for this section, because we usually use datatables with databases with datas passedin the python file

#from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix import screen
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp  # stands for Display Pixels


class MainApp(MDApp):
    def build(self):

        screen = Screen()

        table = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            column_data=[
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Addr", dp(40)),
                ("Phone Num", dp(30))
            ],
            row_data=[
                ("Soheil", "Forouzan", "soheil.forouzan@pm.me", "00989911825644"),
                ("Soheil", "Forouzan", "soheil.forouzan@pm.me", "00989911825644"),
            ]
        )

        # Setting actions for tapping and checking the table rows
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.tapped)

        def checked(self, instance_table, current_row):
            pass

        def tapped(self, instance_table, instance_row):
            pass

        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"  # To set the primary pallet color
        # To set the primary accent color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        # return Builder.load_file('starter.kv')

        screen.add_widget(table)

        return screen


MainApp().run()
