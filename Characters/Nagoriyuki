from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Nagoriyuki(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def fukyo(self, forward):
        if forward:
            self.qcf(Inputs.k)
        else:
            self.qcb(Inputs.k)
    def zarameyuki(self):
        self.qcf(Inputs.s)
    def kamuriyuki(self):
        self.qcb(Inputs.hs)
    def shizuriyuki(self):
        self.dp(Inputs.hs)
    def bloodsuckingUniverse(self):
        self.dp(Inputs.p)
    def wasureyuki(self):
        self.hcbf(Inputs.s)
    def zansetsu(self):
        self.hcbf(Inputs.hs)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)