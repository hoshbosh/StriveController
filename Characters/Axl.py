from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Axl(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def sickleFlash(self, button):
        self.qcf(Inputs.s)
        if button:
            time.sleep(0.05)
            self.press(button)
    def mistFiner(self, button):
        if self.mist_finer:
            self.press(button)
    def winterManis(self):
        self.hcf(Inputs.hs)
    def rainwater(self):
        self.qcb(Inputs.s)
    def snail(self):
        self.qcb(Inputs.hs)
    def axlBomber(self):
        if self.airBorne:
            self.qcf(Inputs.hs)
    def whistlingWind(self):
        self.qcb(Inputs.k)
    def sickleStorm(self):
        self.qcfEmpty()
        self.qcf(Inputs.hs)
    def oneVision(self):
        self.hcbf(Inputs.p)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)



