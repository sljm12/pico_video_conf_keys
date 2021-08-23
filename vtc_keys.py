from adafruit_hid.keycode import Keycode

class GoogleMeet:
    def __init__(self, kbd):
        '''
        kbd a AdaFruit HID Keyboard instance
        '''
        self.kbd = kbd
    def mute(self):
        def t():
            print("Google Meet mute/unmute pressed")
            self.kbd.send(Keycode.LEFT_CONTROL, Keycode.D)
        return t
        
    def camera(self):
        def t():
            print("Google Meet camera pressed")
            self.kbd.send(Keycode.LEFT_CONTROL, Keycode.E)
        return t
    
class Zoom:
    def __init__(self, kbd):
        '''
        kbd a AdaFruit HID Keyboard instance
        '''
        self.kbd = kbd
    def mute(self):
        def t():
            print("Google Meet mute/unmute pressed")
            self.kbd.send(Keycode.ALT, Keycode.A)
        return t
        
    def camera(self):
        def t():
            print("Google Meet camera pressed")
            self.kbd.send(Keycode.ALT, Keycode.V)
        return t
    
    
class ZoomMac:
    def __init__(self, kbd):
        '''
        kbd a AdaFruit HID Keyboard instance
        '''
        self.kbd = kbd
    def mute(self):
        def t():
            print("Zoom Mac mute/unmute pressed")
            self.kbd.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
        return t
        
    def camera(self):
        def t():
            print("Zoom Mac camera pressed")
            self.kbd.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.V)
        return t
    
class BlueJeans:
    def __init__(self, kbd):
        '''
        kbd a AdaFruit HID Keyboard instance
        '''
        self.kbd = kbd
    def mute(self):
        def t():
            print("Blue Jeans mute/unmute pressed")
            self.kbd.send(Keycode.M)
        return t
        
    def camera(self):
        def t():
            print("Blue Jeans Video pressed")
            self.kbd.send(Keycode.V)
        return t