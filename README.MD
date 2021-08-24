Have u ever want to have a seperate set of keys to control your zoom or google meet meetings?

Now you can you just need a Raspberry PI Pico, a set of cheap key switch tester and Circuit Python and your done!

In this Repo is a set of codes that you can upload to your Pico for you to do just that. 

## Parts:
* Raspberry PI Pico flashed with CircuitPython 6.3.0
* Breadboard (if you dont want to solder directly to the pico
* Switch Tester (https://shopee.sg/Gateron-MX-Switch-Acrylic-Mechanical-Keyboards-Switch-4-Translucent-Clear-Sampler-Tester-Kit-Toys-Stress-Relief-Gifts--i.135054553.2628487640)
* Wires

![Back of the Switch](/images/back.jpg)
_Back of the switches you can see there are 2 pins for each switch._

![wiring](/images/wiring.png)
_I wired the top line of contacts as the gound and the other as the Digital Read line. I cut a 22AWG wire and stip the insulation in between in order to just use one long wite to connect the groud._

![wiring](/images/Finished.jpg)
_The finished look_

## Steps:
* Clone this repository
* Rename test_button.py to code.py if you want to run this automatically when the Pico is plug in
* Configure the code to load the correct set of keycodes

## Modifying the keys
You can look at vtc_codes.py to see a sample of how to add new key codes or to expand it.


