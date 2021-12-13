from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class MainApp(MDApp):

    dialog = None  # So we make sure that the dialog box is closed by default :)

    def build(self):
        # Makes the overall app theme Dark(default = Light)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"  # To set the primary pallet color
        # To set the primary accent color. Visit https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py for more icons
        return Builder.load_file('dialog.kv')

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Title goes here",
                text = "The text goes here",
                buttons = [
                    MDFlatButton(
                        text='cancel',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text='ok',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.label_dialog
                    ),
                    # Go to https://github.com/kivymd/KivyMD/tree/master/kivymd/uix/button for more buttons
                ],
            )  # Since we are adding the dialog box directly in the python file, we need to import some tools

        self.dialog.open()
        
    # To close th alert dialog
    def close_dialog(self, obj):
        self.dialog.dismiss()

    # To approve the dilog popup
    def label_dialog(self, obj):
        self.dialog.dismiss()

        self.root.ids.my_label.text = "Approved!"


MainApp().run()
