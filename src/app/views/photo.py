from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.graphics import texture
import numpy as np



class PhotoView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.my_images = []
        
    def take_photo(self):
        self.counter = 1
        self.update_counter()

    def update_counter(self, *args):
        if self.counter <= 3:

            if self.counter == 3:
                self.ids.counter_label.text = "YA!"
            else:
                self.ids.counter_label.text = str(self.counter)

            self.animate_counter()
            self.counter += 1
            Clock.schedule_once(self.update_counter, 1.0)
        else:
            self.ids.counter_label.text = ""
            self.counter = 1

            # process image
            texture = self.ids.camera.texture
            buffer = texture.pixels
            texture_size = texture.size
            img = np.frombuffer(buffer, dtype=np.uint8).reshape(texture_size[1], texture_size[0], 4)
            
            # save image
            self.my_images.append(img)

            if len(self.my_images) == 3:
                third = self.manager.get_screen("third")
                third.show_images(self.my_images)
                self.manager.current = 'third'
                self.my_images = []
            else:
                Clock.schedule_once(self.update_counter, 2.0)
            

    def animate_counter(self, *args):
        anim = Animation(font_size=300, duration=0.5) + Animation(font_size=80, duration=0.5)
        anim.start(self.ids.counter_label)