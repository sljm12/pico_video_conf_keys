import usb_hid
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
import time
from vtc_keys import GoogleMeet, Zoom, ZoomMac, BlueJeans, WebEx

kbd = Keyboard(usb_hid.devices)

class Button:
    def __init__(self, gpPin):
        self.pin = DigitalInOut(gpPin)
        self.pin.direction=Direction.INPUT
        self.pin.pull = Pull.UP
        self.pressed = False
        self.action = None
    
    def check_pressed(self):
        if self.pin.value == False and self.pressed == False:
            self.pressed = True
            self.action()
        elif self.pin.value == True and self.pressed == True:
            self.pressed= False

def b1_action():
    print("b1 pressed")
    kbd.send(Keycode.LEFT_CONTROL, Keycode.D)

def b2_action():
    print("b2 pressed")
    kbd.send(Keycode.ALT, Keycode.V)

gm = WebEx(kbd)

b1 = Button(board.GP2)
b1.action = gm.mute()

b2 =  Button(board.GP8)
b2.action = gm.camera()


while True:
    b1.check_pressed()
    b2.check_pressed()
    time.sleep(0.1)
