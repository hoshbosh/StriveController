from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Zato_1(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def summonEddie(self):
        self.qcb(Inputs.hs)
    def pierce(self):
        self.qcf(Inputs.p)
    def thatsALot(self):
        self.qcf(Inputs.k)
    def leap(self):
        self.qcf(Inputs.s)
    def oppose(self, button):
        self.qcf(Inputs.hs)
    def inviteHell(self):
        self.press(self.dir.down)
        time.sleep(0.05)
        self.press(self.dir.down, Inputs.hs)
    def breakTheLaw(self, teleport):
        self.qcb(Inputs.k)
        if teleport:
            self.press(self.dir.down)
            time.sleep(0.05)
            self.press(self.dir.down)
    def damnedFang(self):
        self.dp(Inputs.s)
    def drunkardShade(self):
        self.qcb(Inputs.s)
    def amorphous(self):
        self.hcbf(Inputs.hs)
    def sunVoid(self):
        self.hcbf(Inputs.s)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)