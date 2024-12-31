from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Chipp(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def alphaBlade(self, button):
        self.qcf(button)
    def betaBlade(self):
        self.dp(Inputs.s)
    def gammaBlade(self):
        self.qcf(Inputs.hs)
    def resshou(self):
        self.qcf(Inputs.s)
    def rokusai(self):
        self.qcf(Inputs.s)
    def senshuu(self):
        self.qcf(Inputs.k)
    def genrouZan(self):
        self.hcb(Inputs.s)
    def shuriken(self):
        self.qcb(Inputs.p)
    def tightrope(self):
        self.qcb(Inputs.hs)
    def zanseiRouga(self):
        self.hcbf(Inputs.hs)
    def bankiMessai(self):
        self.qcfEmpty()
        self.qcf(Inputs.p)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)