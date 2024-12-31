from Utils.Character import Character
import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Giovanna(Character):
    def __init__(self, _leftRight):
        super().__init__(_leftRight)
    def sepultura(self):
        self.qcb(Inputs.k)
    def travao(self):
        self.qcf(Inputs.k)
    def chave(self):
        self.qcb(Inputs.hs)
    def tempestade(self):
        self.qcfEmpty()
        self.qcf(Inputs.hs)
    def enTravao(self):
        self.chave()
        time.sleep(0.25)
        self.press(self.dir.forward, Inputs.k)
    def enDP(self):
        self.chave()
        time.sleep(0.25)
        self.press(self.dir.forward, Inputs.s)
    def enFlip(self):
        self.chave()
        time.sleep(0.25)
        self.press(self.dir.back, Inputs.s)
    def enSepultura(self):
        self.chave()
        time.sleep(0.25)
        self.press(self.dir.back, Inputs.k)
    def flip(self):
        self.qcb(Inputs.s)
    def ventania(self):
        self.hcbf(Inputs.hs)
    def nascente(self):
        self.dp(Inputs.s)
    def h6(self):
        self.press(self.dir.forward, Inputs.hs)