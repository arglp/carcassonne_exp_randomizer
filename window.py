import tkinter as tk
from interface import Button

class Window:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__root = tk.Tk()
        self.set_geometry()
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=tk.BOTH, expand=1)
        self.__root.title("Carcassone expansion randomizer")
        self.__images = []
        self.__grid = [Point(135, 160), Point(285, 160), Point(60, 235), Point(210, 235), Point(360, 235)]

    def loop(self):
        self.__root.mainloop()

    def set_geometry(self):
        self.__root.geometry(f"{self.__width}x{self.__height}+{200}+{200}")

    def draw_images(self, images):
        self.draw_image(0, images)

    def draw_image(self, i, images):
        if i < len(images):
            img = tk.PhotoImage(file=images[i])
            self.__images.append(img)
            self.__canvas.create_image(self.__grid[i].x, self.__grid[i].y, image=img)
            self.__root.after(1000, lambda: self.draw_image(i + 1, images))

    def delete_images(self):
        self.__images = []

    def place_button(self, button):
        button.draw_button(self.__root, self.__canvas, 210, 50)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


