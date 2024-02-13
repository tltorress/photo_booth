from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from views.start import StartView
from views.photo import PhotoView
from views.final import FinalView
from kivy.lang.builder import Builder

Builder.load_file("src/app/views/photo.kv")
class MVCApp(App):
    def build(self):
        Window.size = (1280, 800)
        screen_manager = ScreenManager()

        first_view = StartView(name='first')
        second_view = PhotoView(name='second')
        third_view = FinalView(name='third')

        screen_manager.add_widget(first_view)
        screen_manager.add_widget(second_view)
        screen_manager.add_widget(third_view)

        return screen_manager

if __name__ == "__main__":
    MVCApp().run()
