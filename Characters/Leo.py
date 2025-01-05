from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Leo(Character):
    backTurn=False
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
        self.backTurn=False
    def gravierteWurde(self, button):
        for x in range(30):
            self.press(self.dir.back)
        self.press(self.dir.forward, button)
    def eisensturm(self, button):
        for x in range(30):
            self.press(self.dir.down)
        self.press(self.dir.up, button)
    def EKG(self):
        self.qcf(Inputs.s)
    def ZKG(self):
        self.qcf(Inputs.hs)
    def turbulenz(self):
        self.qcb(Inputs.s)
    def glanzendesDunkel(self):
        if self.backTurn:
            self.qcb(Inputs.k)
    def blitzschlag(self):
        if self.backTurn:
            self.qcb(Inputs.hs)
    def cancel(self):
        self.press(self.dir.down)
        time.sleep(0.05)
        self.press(self.dir.down)
    def stahlwirbel(self):
        if self.backTurn:
            self.hcbf(Inputs.s)
    def LdD(self):
        self.hcbf(Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)


