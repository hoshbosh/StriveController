from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Slayer(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def mappyHunch(self, button):
        self.qcf(button)
    def dandyStep(self, button, followup):
        self.qcf(button)
        if followup:
            time.sleep(0.05)
            self.press(followup)
    def bloodsuckingUniverse(self):
        self.hcb(Inputs.hs)
    def handOfDoom(self):
        self.press(Inputs.s, self.dir.forward)
    def superMappaHunch(self):
        self.hcbf(Inputs.s)
    def lastHorizon(self):
        self.qcfEmpty()
        self.qcf(Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)

