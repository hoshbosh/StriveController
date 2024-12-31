from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class ky(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def stunEdge(self):
        self.qcf(Inputs.s)
    def chargedStunEdge(self):
        self.qcf(Inputs.hs)
    def stunDipper(self):
        self.qcf(Inputs.k)
    def foudreArc(self):
        self.qcb(Inputs.k)
    def vaporThrust(self, button):
        self.dp(button)
    def direEclat(self):
        self.qcb(Inputs.s)
    def RTL(self):
        self.hcbf(Inputs.hs)
    def sacredEdge(self):
        self.qcfEmpty()
        self.qcf(Inputs.p)
    def DI(self):
        self.qcbEmpty()
        self.qcb(Inputs.h)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)