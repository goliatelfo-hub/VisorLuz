from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
Window.clearcolor = (0,0,0,1)

class VisorLuz(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text='[b]VisorLuz v9.7 HIBRIDA[/b]', markup=True, font_size=28))
        self.add_widget(Label(text='Modo Visor + Linterna listo', font_size=18))
        btn = Button(text='ACTIVAR LUZ', size_hint=(1,0.3), background_color=(1,1,0,1))
        btn.bind(on_press=self.flash)
        self.add_widget(btn)
        self.lbl = Label(text='Esperando...')
        self.add_widget(self.lbl)
    def flash(self, *a):
        self.lbl.text = 'LUZ ACTIVADA - v9.7'

class VisorLuzApp(App):
    def build(self):
        return VisorLuz()

VisorLuzApp().run()
