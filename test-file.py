class Toybox():
    def __init__(self, toy):
        self._toy = None
        self.toy = toy

    @property
    def toy(self):
        return self._toy # the🔒LOCK shows what toy is inside


    @toy.setter
    def toy(self, new_toy):
        if len(new_toy) > 10: # lets say toys longer than 10 units are too big
            raise ValueError("This toy is too big!")

        self._toy = new_toy # Put the toy in the box

