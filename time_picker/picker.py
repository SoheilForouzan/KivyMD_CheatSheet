from datetime import date
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker


class MainApp(MDApp):
    def build(self):
        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Light" # NOTE: Pickers are more visible in light mode :)
        self.theme_cls.primary_palette = "Blue"  # To set the primary pallet color

        # To set the primary accent color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        return Builder.load_file('picker.kv')

    def open_time_picker(self):
        from datetime import datetime

        # Set default time
        default_time = datetime.strptime("1:30:17", "%H:%M:%S").time()

        time_dialog = MDTimePicker()

        # Use the defalt time
        time_dialog.set_time(default_time)
        time_dialog.bind(time=self.get_time, on_cancel=self.on_cancel)
        time_dialog.open()

    # Gets time
    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)

    # Cancel Clicked
    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "Canceled"
        print("soheil")

MainApp().run()
