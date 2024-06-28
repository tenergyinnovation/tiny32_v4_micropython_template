# main.py -- put your code here!
from tiny32_v3 import tiny32_v3
from time import sleep


state = False
while True:

    if tiny32_v3.Sw1():
        print("Sw1 is pressing")
        tiny32_v3.Buzzer_beep(1)
        while tiny32_v3.Sw1():
            pass
        state = ~state
        tiny32_v3.Relay(state)
        tiny32_v3.RedLED(state)
        tiny32_v3.BlueLED(not state)
        tiny32_v3.BuildInLED(state)
        print(tiny32_v3.Slid_Sw())
        print(f"Slide switch =>  {tiny32_v3.Slid_Sw()}")

    if tiny32_v3.Sw2():
        print("Sw2 is pressing")
        tiny32_v3.Buzzer_beep(1)
        while tiny32_v3.Sw2():
            pass
        state = ~state
        tiny32_v3.Relay(state)
        tiny32_v3.RedLED(state)
        tiny32_v3.BlueLED(not state)
        tiny32_v3.BuildInLED(state)
        print(f"Slide switch =>  {tiny32_v3.Slid_Sw()}")

    sleep(0.1)
