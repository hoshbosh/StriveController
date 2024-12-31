from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Sol(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def gunFlame(self):
        self.qcf(Inputs.p)
    def gunFlameFeint(self):
        self.qcb(Inputs.p)
    def dpS(self, button):
        self.dp(button)
    def banditRevolver(self):
        self.qcf(Inputs.k)
    def banditBringer(self):
        self.qcb(Inputs.k)
    def wildThrow(self):
        self.dp(Inputs.k)
    def nightRaidVortex(self):
        self.qcb(Inputs.s)
    def fafnir(self):
        self.hcf(Inputs.hs)
    def tyrantRave(self):
        self.hcbf(Inputs.hs)
    def heavyModCemetery(self):
        self.qcbEmpty()
        self.qcb(Inputs.hs)
    def s6(self):
        self.press(self.dir.forward, Inputs.s)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
