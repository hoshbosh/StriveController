from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Johnny(Character):
    mist_finer=False
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
        self.backTurn=False
    def mistFinerStance(self, button):
        self.qcb(button)
        mist_finer=True
    def mistFiner(self, button):
        if self.mist_finer:
            self.press(button)
    def deal(self, button):
        if self.airBorne:
            self.qcf(Inputs.hs)
        else:
            self.qcf(button)
    def vault(self, deal):
        self.qcf(Inputs.hs)
        if deal:
            time.sleep(0.05)
            self.press(Inputs.hs)
    def ensenga(self):
        self.qcb(Inputs.hs)
    def TMN(self):
        self.hcbf(Inputs.hs)
    def jokerTrick(self):
        self.qcfEmpty()
        self.qcf(Inputs.s)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)


