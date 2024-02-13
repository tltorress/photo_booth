from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class StartView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text="HAZ CLICK PARA COMENZAR!")
        self.add_widget(self.label)
        self.bind(on_touch_down=self.change_view)

    def change_view(self, *args):
        self.manager.current = 'second'