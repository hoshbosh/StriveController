from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Ramlethal(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def ondo(self):
        self.qcf(Inputs.k)
    def dauro(self):
        self.dp(Inputs.p)
    def erarlumo(self):
        self.qcb(Inputs.p)
    def sildoDetruo(self):
        self.qcb(Inputs.k)
    def bajoneto(self, button):
        self.qcf(button)
    def agresaOrdono(self):
        self.qcb(Inputs.s)
    def sabrobato(self):
        self.qcb(Inputs.hs)
    def calvados(self):
        self.hcbf(Inputs.hs)
    def mortobato(self):
        self.qcfEmpty()
        self.qcf(Inputs.s)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)