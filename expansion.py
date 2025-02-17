from settings import Settings

class Expansion:
    def __init__(self, type, nr, de, es, count):
        self.id = f"{type}-{nr}"
        self.type = type
        self.nr = nr
        self.de = de
        self.es = es
        self.play_count = int(count)
        self.img = f"{Settings().src_dir_img}/{self.id}.png"
        