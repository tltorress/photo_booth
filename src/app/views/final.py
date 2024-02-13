from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.graphics.texture import Texture
import cv2

class FinalView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
    def show_images(self, images):
        roll = cv2.imread('src/assets/images/roll.jpg')
        gray = cv2.cvtColor(roll, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        green_squares = []
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
            if len(approx) == 4 and cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                green_squares.append((x, y, w, h))
        
        for i, (x, y, w, h) in enumerate(green_squares):
            resized_image = cv2.resize(images[i], (w, h))

            if resized_image.shape[2] == 4:
                resized_image = resized_image[:, :, :3]

            roll[y:y+h, x:x+w] = resized_image

        roll = cv2.rotate(roll, cv2.ROTATE_180)

        buffer = roll.tobytes()
        size = roll.shape[1], roll.shape[0]
        texture = Texture.create(size=size)
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')

        self.kivy_image = Image(texture=texture)
        
        self.layout = BoxLayout()
        self.layout.add_widget(self.kivy_image)

        self.add_widget(self.layout)