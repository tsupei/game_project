import tkinter as tk
from PIL import ImageTk, Image

def _load_image(filename, height, width):
    raw = Image.open(filename)
    raw = raw.resize((height, width))
    img = ImageTk.PhotoImage(raw)
    return img

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, height=600, width=600, bg="white")
        
        self._load_images()
        self._create_helicopter()
        self._bind_events()

        self.canvas.pack()


    def _load_images(self):
       self.helicopter_image = _load_image("./src/helicopter.png", 50, 50)
       self.bullet_image = _load_image("./src/bullet.png", 15, 15)

    def _create_helicopter(self):
        self.helicopter = self.canvas.create_image(100, 100, image=self.helicopter_image)

    def _bind_events(self):
        self.master.bind("<space>", self.shoot)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

    def move_left(self, event):
        self.canvas.move(self.helicopter, -10, 0)
        self.canvas.update()

    def move_right(self, event):
        self.canvas.move(self.helicopter, 10, 0)
        self.canvas.update()

    def move_up(self, event):
        self.canvas.move(self.helicopter, 0, -10)
        self.canvas.update()

    def move_down(self, event):
        self.canvas.move(self.helicopter, 0, 10)
        self.canvas.update()
   
    def shoot(self, event):
        offset = self.canvas.coords(self.helicopter)
        x = offset[0] + 50
        y = offset[1]
        bullet = self.canvas.create_image(x, y, image=self.bullet_image)
        self.canvas.after(10, lambda: self.shoot_animation(bullet))

    def shoot_animation(self, bullet):
        self.canvas.move(bullet, 10, 0)
        if self.canvas.coords(bullet)[0] < 650:
            self.canvas.after(10, lambda: self.shoot_animation(bullet=bullet))
        else:
            self.canvas.delete(bullet)

