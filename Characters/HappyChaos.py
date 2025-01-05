from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class HappyChaos(Character):
    ATR=False
    STEADY_AIM=False
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def ATRh(self):
        self.press(Inputs.hs)
        atr=True
    def ATRs(self):
        self.qcf(Inputs.s)
        atr=True
    def steadyAim(self):
        self.qcb(Inputs.s)
        self.STEADY_AIM=True
    def fire(self):
        if self.STEADY_AIM:
            self.press(Inputs.hs)
    def cancelAim(self):
        if self.ATR:
            self.press(self.dir.down, self.press(Inputs.hs))
        elif self.STEADY_AIM:
            self.press(self.dir.back, self.press(Inputs.s))
    def reload(self):
        if self.STEADY_AIM:
            self.press(self.dir.down, Inputs.p)
        else:
            self.press(self.dir.down)
            time.sleep(0.05)
            self.press(self.dir.down, Inputs.p)
    def focus(self):
        if self.STEADY_AIM:
            self.press(self.dir.back, Inputs.p)
        else:
            self.qcb(Inputs.p)
    def curse(self):
        if self.STEADY_AIM:
            self.press(self.dir.forward, Inputs.p)
        else:
            self.qcf(Inputs.p)
    def scapeGoat(self):
        if self.STEADY_AIM:
            self.press(self.dir.forward, Inputs.k)
        else:
            self.qcf(Inputs.k)
    def roll(self):
        if self.STEADY_AIM:
            self.press(self.dir.back, Inputs.k)
        else:
            self.qcb(Inputs.k)
    def DEM(self):
        self.hcbf(Inputs.s)
    def superFocus(self):
        self.qcbEmpty()
        self.qcb(Inputs.p)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)
    def s6(self):
        self.press(self.dir.forward, Inputs.s)