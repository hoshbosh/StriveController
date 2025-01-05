from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Jacko(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def servantShoot(self):
        self.qcf(Inputs.k)
    def summonServant(self):
        self.qcb(Inputs.p)
    def releaseServant(self):
        self.press(Inputs.d)
    def recoverServant(self):
        self.qcb(Inputs.p)
    def attackCommand(self):
        self.qcb(Inputs.k)
    def defendCommand(self):
        self.qcb(Inputs.s)
    def countDown(self):
        self.qcb(Inputs.hs)
    def FED(self):
        self.hcbf(Inputs.p)
    def CSO(self, button):
        self.qcfEmpty()
        self.qcf(Inputs.hs)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def throwServant(self, button):
        self.press(self.dir.forward, button)