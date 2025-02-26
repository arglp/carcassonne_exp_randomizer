from randomizer import Randomizer
from window import Window
from settings import Settings
from interface import Button

def main():
    print("Starting Carcassonne Expansion Randomizer...")

    settings = Settings()
    win = Window(settings.win_heigth, settings.win_width)
    randomizer = Randomizer(win, settings)

    main_btn = Button("Sortear", randomizer.randomize)
    win.place_button(main_btn)


    win.loop()

if __name__ == "__main__":
    main()
