from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class potemkin(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def potemkinBuster(self):
        self.hcbf(Inputs.p)
    def heatKnuckle(self):
        self.dp(Inputs.hs)
    def megafist(self, forward):
        if forward:
            self.qcf(Inputs.p)
        else:
            self.qcb(Inputs.p)
    def slideHead(self):
        self.qcf(Inputs.s)
    def hammerFall(self):
        for x in range(10):
            self.press(self.dir.back)
        self.press(self.dir.forward, Inputs.hs)
    def fdb(self):
        self.qcb(Inputs.k)
    def garudaImpact(self):
        self.qcb(Inputs.hs)
    def heatTacke(self):
        self.dp(Inputs.k)
    def hpb(self):
        self.hcbf(Inputs.s)
    def giganterKai(self):
        self.hcbf(Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)

