from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Sin(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def beakDriver(self):
        self.qcf(Inputs.hs)
    def hawkBaker(self):
        self.dp(Inputs.s)
    def elkHunt(self):
        self.qcf(Inputs.k)
    def hoofStomp(self):
        self.qcb(Inputs.s)
    def gazelleStep(self):
        self.qcb(Inputs.k)
    def stillGrowing(self):
        self.hcb(Inputs.p)
    def RTL(self):
        self.hcbf(Inputs.hs)
    def tyrantBarrel(self):
        self.qcfEmpty()
        self.qcf(Inputs.p)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)