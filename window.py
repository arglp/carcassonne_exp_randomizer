import tkinter as tk

class Window:
    def __init__(self, height, width):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=tk.BOTH, expand=1)
        self.__root.title("Carcassone expansion randomizer")
        self.__images = []
        self.__grid = [Point(135, 60), Point(285, 60), Point(60, 135), Point(210, 135), Point(360, 135)]

    def loop(self):
        self.__root.mainloop()

    def draw_image(self, i, file):
        print(f"drawing {file}")
        img = tk.PhotoImage(file=file)
        self.__images.append(img)
        self.__canvas.create_image(self.__grid[i].x, self.__grid[i].y, image=img)     

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


