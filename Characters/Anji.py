from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Anji(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def shitsu(self):
        self.qcf(Inputs.p)
    def SNH(self):
        self.qcf(Inputs.k)
    def midare(self):
        self.qcb(Inputs.p)
    def fuujin(self, followup):
        self.qcf(Inputs.hs)
        if followup:
            time.sleep(0.1)
            self.press(followup)
    def kou(self):
        self.qcf(Inputs.s)
    def IOS(self):
        self.hcbf(Inputs.hs)
    def KK(self):
        self.hcbf(Inputs.s)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)