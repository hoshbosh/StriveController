import time
import vgamepad as vg
from Utils.Inputs import Inputs
class Dirs():
    up=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
    down=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    def __init__(self, leftRight):
        if leftRight:
            self.forward=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
            self.back=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
        else:
            self.forward=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
            self.back=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

class Character: 
    dir: Dirs
    airBorne:bool
    pad: vg.VX360Gamepad
    def __init__(self, _leftRight):
        self.dir=Dirs(_leftRight)
        self.pad=vg.VX360Gamepad()
        time.sleep(5)
        airBorne=False
        # self.press(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        print("gamepad made")
    def press(self, *args):
        for button in args:
            if button=="RT":
                self.pad.right_trigger_float(1.0)
            else:
                self.pad.press_button(button)
        self.pad.update()
        time.sleep(0.016)
        for button in args:
            if button=="RT":
                self.pad.right_trigger_float(0.0)
            else:
                self.pad.release_button(button)
        self.pad.update()
    def qcf(self, button):
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.forward)
        self.press(self.dir.forward, button)
    def jump(self):
        self.press(self.dir.up)
    def qcfEmpty(self):
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.forward)
        self.press(self.dir.forward)
    def qcb(self, button):
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.back)
        self.press(self.dir.back, button)
    def qcbEmpty(self):
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.back)
        self.press(self.dir.back)
    def hcbf(self, button):
        self.press(self.dir.forward)
        self.press(self.dir.down, self.dir.forward)
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.back)
        self.press(self.dir.back)
        self.press(self.dir.forward, button)
    def hcb(self, button):
        self.press(self.dir.forward)
        self.press(self.dir.down, self.dir.forward)
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.back)
        self.press(self.dir.back, button)
    def hcf(self, button):
        self.press(self.dir.back)
        self.press(self.dir.down, self.dir.back)
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.forward)
        self.press(self.dir.forward)
    def dp(self, button):
        self.press(self.dir.forward)
        self.press(self.dir.down)
        self.press(self.dir.down, self.dir.forward, button)
    def block(self, crouch, fd):
        buttons=[]
        if crouch: 
            buttons.append(self.dir.down)
        if fd:
            buttons.append(Inputs.s)
            buttons.append(Inputs.hs)
        buttons.append(self.dir.back)
        self.press(*buttons)
        print("blocked")
    def WA(self):
        self.qcf(Inputs.d)
    def dash(self):
        self.press(self.dir.forward)
        time.sleep(0.05)
        self.press(self.dir.forward)
    def backDash(self):
        self.press(self.dir.back)
        time.sleep(0.05)
        self.press(self.dir.back)
    def deflectShield(self):
        self.qcb(Inputs.d)
    def rc(self):
        self.press(Inputs.p, Inputs.k, Inputs.s)
    def p6(self):
        self.press(self.dir.forward, Inputs.p)
    def p2(self):
        self.press(self.dir.down, Inputs.p)
    def k2(self):
        self.press(self.dir.down, Inputs.k)
    def s2(self):
        self.press(self.dir.down, Inputs.s)
    def d2(self):
        self.press(self.dir.down, Inputs.d)
    def h2(self):
        self.press(self.dir.down, Inputs.hs)