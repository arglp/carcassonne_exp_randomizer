from settings import Settings
from window import Window
from expansion import Expansion
import random

class Randomizer:
    def __init__ (self, win, settings):
        self.settings = settings
        self.win = win
        self.exp_list, self.headings = self.read_src()
        self.elect_list = []

    def read_src(self):
        with open(self.settings.src_exp, encoding=self.settings.src_exp_encoding) as file:
            text = file.read()
            headings = text.splitlines()[0].split(";")
            lines = text.splitlines()[1:]
            list = []
        for line in lines:
            fields = line.split(";")
            list.append(Expansion(*fields))
        return(list, headings)
    
    def write_src(self):
        with open(self.settings.src_exp, "w") as file:
            print("writing src")
            file.write(";".join(self.headings))
            for exp in self.exp_list:
                file.write(f"\n{exp.type};{exp.nr};{exp.de};{exp.es};{exp.play_count};{exp.weight};{exp.bias}")

    def randomize(self):
        self.elect_list = []
        self.win.delete_images()
        if self.settings.method == 0:
            self.basic_randomization()
        if self.settings.method == 1:
            self.adaptive_randomization()
        print("Selected expansions:")
        for elect in self.elect_list:
            elect.play_count += 1
            elect.weight += 1
            print(f"{elect.es}: {elect.play_count}")
        self.reset_weight()
        self.write_src()
        self.draw_images()

    def draw_images(self):
        images = []
        for exp in self.elect_list:
            images.append(exp.img)
        self.win.draw_images(images)


    def basic_randomization(self):
        print("Starting basic randomization process...")
        random_numbers = random.sample(range(len(self.exp_list)), self.settings.exp_elect_nr)
        for num in random_numbers:
            self.elect_list.append(self.exp_list[num])

    def adaptive_randomization(self):
        print("Starting adaptive randomization process...")
        exp_pool = []
        for exp in self.exp_list:
            if exp.weight <= len(self.exp_list):
                temp_list = [exp] * (len(self.exp_list) - exp.weight)
                exp_pool.extend(temp_list)
            else:
                exp_pool.extend([exp])
        while len(self.elect_list) < self.settings.exp_elect_nr:
            chosen = exp_pool[random.randrange(len(exp_pool))]
            if chosen not in self.elect_list and chosen.bias == -1:
                num = random.randint(0, 3)
                if num == 1:
                    self.elect_list.append(chosen)
            elif chosen not in self.elect_list:
                    self.elect_list.append(chosen)
    
    def reset_weight(self):
        not_maxed = 0
        for exp in self.exp_list:
            if exp.weight < len(self.exp_list):
                not_maxed += 1
        if not_maxed < 5:
            for exp in self.exp_list:
                exp.weight = 0