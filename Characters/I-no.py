from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class I_no(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def antidepressantScale(self):
        self.qcb(Inputs.p)
    def stroke(self, button):
        self.qcf(button)
    def sultryPerformance(self, button):
        self.qcf(button)
    def chemicalLove(self):
        self.qcb(Inputs.k)
    def madLoveAgitato(self):
        self.qcb(Inputs.s)
    def megalomania(self):
        self.hcbf(Inputs.hs)
    def ultimateFortissimo(self):
        self.hcbf(Inputs.s)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)

