from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class May(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def totsu(self, button):
        for x in range(30):
            self.press(self.dir.back)
        self.press(self.dir.forward, button)
    def totsuVertical(self, button):
        for x in range(30):
            self.press(self.dir.down)
        self.press(self.dir.up, button)
    def overheadKiss(self):
        self.dp(Inputs.k)
    def arisugawaSparkle(self, button):
        self.qcb(button)
    def GYA(self):
        self.qcfEmpty()
        self.qcf(Inputs.s)
    def killerWhale(self):
        self.hcbf(Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)
    def h3(self):
        self.press(self.dir.forward, self.dir.down, Inputs.k)



