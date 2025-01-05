from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Elphelt(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def missCharlotte(self, button):
        self.qcf(button)
    def backShot(self):
        self.qcb(Inputs.k)
    def BBC(self):
        self.qcb(Inputs.hs)
    def HIG(self):
        self.qcf(Inputs.hs)
    def JDP(self):
        self.hcbf(Inputs.hs)
    def BB(self):
        self.qcfEmpty()
        self.qcf(Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)