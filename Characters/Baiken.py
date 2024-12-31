from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Baiken(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def tatamiGaeshi(self):
        self.qcf(Inputs.k)
    def kabari(self, button):
        self.hcf(button)
    def youzansen(self):
        self.qcf(Inputs.s)
    def hiigari(self):
        self.qcf(Inputs.p)
    def tsuraneSanzuWatashi(self):
        self.qcfEmpty()
        self.qcf(Inputs.s)
    def kenjyu(self):
        self.qcbEmpty()
        self.qcb(Inputs.p)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)