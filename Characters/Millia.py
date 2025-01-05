from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Millia(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def tandemTop(self, button):
        self.qcb(button)
    def badMoon(self):
        if self.airBorne:
            self.qcf(Inputs.p)
    def ironSavior(self, button):
        self.qcb(Inputs.p)
    def turboFall(self):
        if self.airBorne:
            self.qcf(Inputs.k)
    def mirazh(self, followup):
        self.qcb(Inputs.k)
        if followup:
            time.sleep(0.05)
            self.press(followup)
    def lustShaker(self):
        self.qcb(Inputs.s)
    def artemis(self):
        self.qcb(Inputs.hs)
    def kapel(self):
        if self.airborne:
            self.qcf(Inputs.hs)
    def kapel(self):
        self.hcbf(Inputs.hs)
    def septemVoices(self):
        self.qcfEmpty()
        self.qcf(Inputs.s)
    def k6(self):
        self.press(self.dir.forward, Inputs.k)
    def h6(self):
        self.press(self.dir.forward, Inputs.h)



