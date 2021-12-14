from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

class MainApp(MDApp):
    def build(self):
        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"  # To set the primary pallet color
        # To set the primary accent color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        return Builder.load_file('picker.kv')

    def open_picker(self):
        date_dialog = MDDatePicker(
            #year=2000, month=2, day=14, # In order to pick a default date
            mode = "range",
            )

        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # Ok Clicked
    def on_save(self, instance, value, date_range):
        # Use one of below examples to execute some basic code (comment <pass>)

        #self.root.ids.date_label.text = str(value)
        self.root.ids.date_label.text = str(date_range) # This will return a list of picked dates

    # Cancel Clicked
    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = "Canceled"

MainApp().run()
