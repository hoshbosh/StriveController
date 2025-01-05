from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Bridget(Character):
    yoyo_out=False
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def stopAndDashOut(self, button):
        self.qcf(button)
        self.yoyo_out=True
    def stopAndDashReturn(self, button):
        self.qcf(button)
        self.yoyo_out=True
    def rollingMovement(self):
        if self.yoyo_out:
            self.qcb(Inputs.k)
    def starship(self):
        self.dp(Inputs.p)
    def KSMH(self):
        self.qcf(Inputs.k)
    def rogerDive(self):
        if self.airBorne:
            self.qcf(Inputs.k)
    def RtB(self):
        self.hcb(Inputs.p)
    def LtL(self):
        self.hcbf(Inputs.s)
    def RKM(self):
        self.hcbf(Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)



