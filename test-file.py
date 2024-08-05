class Toybox():
    def __init__(self, toy):
        self._toy = None
        self.toy = toy

    @property
    def toy(self):
        return self._toy # the🔒LOCK shows what toy is inside