import tkinter as tk

class Window:
    def __init__(self, height, width):
        self.__root = tk.Tk()
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=tk.BOTH, expand=1)
        self.__root.title("Carcassone expansion randomizer")
        self.__images = []

    def loop(self):
        self.__root.mainloop()

    def draw_image(self, x, y, file):
        print(f"drawing {file}")
        img = tk.PhotoImage(file=file)
        self.__images.append(img)
        self.__canvas.create_image(x, y, image=img)


