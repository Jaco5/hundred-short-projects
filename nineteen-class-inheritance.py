#phylogeny project of some kind?


class Eukarya():
    def ___init___(self):
        organelles = True
        nucleus = True

    def divide(self):
        print("New cells!")

class Animalia(Eukarya):
    def ___init___(self):
        super().___init___()

    def meiosis(self):
        print("New baby")


manny = Animalia()
manny.divide()
manny.meiosis()
