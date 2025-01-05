from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Testament(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def graveReaper(self, button):
        self.qcf(button)
    def unholyDiver(self):
        self.qcb(Inputs.p)
    def possession(self):
        self.qcb(Inputs.k)
    def arbiterSign(self, button):
        self.qcb(button)
    def nostrovia(self):
        self.qcfEmpty()
        self.qcf(Inputs.p)
    def calamityOne(self):
        self.qcfEmpty()
        self.qcf(Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)