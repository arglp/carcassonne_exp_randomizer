from settings import Settings
from window import Window
from expansion import Expansion
import random

class Randomizer:
    def __init__ (self):
        self.settings = Settings()
        self.exp_list, self.headings = self.read_src()
        self.win = Window(self.settings.win_heigth, self.settings.win_width)
        self.elect_list = []
        self.randomize()
        self.win.loop()

    def read_src(self):
        with open(self.settings.src_exp, encoding=self.settings.src_exp_encoding) as file:
            text = file.read()
            headings = text.splitlines()[0].split(";")
            lines = text.splitlines()[1:]
            list = []
        for line in lines:
            fields = line.split(";")
            dict = {}
            for i in range(0, len(headings)):
                dict[headings[i]] = fields[i]
            list.append(Expansion(dict["type"], dict["nr"], dict["de"], dict["es"], dict["play_count"]))
        return(list, headings)
    
    def write_src(self):
        with open(self.settings.src_exp, "w") as file:
            print("writing src")
            file.write(";".join(self.headings))
            for exp in self.exp_list:
                file.write(f"\n{exp.type};{exp.nr};{exp.de};{exp.es};{exp.play_count}")

    def randomize(self):
        print("Starting to randomization proces...")
        random_numbers = random.sample(range(len(self.exp_list)), self.settings.exp_elect_nr)
        for num in random_numbers:
            self.elect_list.append(self.exp_list[num])
        print("Selected expansions:")
        for elect in self.elect_list:
            elect.play_count += 1#
            print(f"{elect.es}: {elect.play_count}")
        self.write_src()
        self.draw_images()

    def draw_images(self):
        print("Drawing_images:")
        for i in range(len(self.elect_list)):
            self.win.draw_image(100 + 120 * i, 100, self.elect_list[i].img)