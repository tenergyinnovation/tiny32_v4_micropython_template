from machine import Pin
from time import sleep

version = 0.1
SW1_PIN = 34
SW2_PIN =  35
RELAY_PIN =  25
LED_IO4_PIN =  4  #blueLED
LED_IO12_PIN = 12 #redLED
LED_BUILDIN = 2
SLID_SW_PIN = 36
BUZZER_PIN = 13
RXD2_PIN = 16
TXD2_PIN = 17
Relay_Value = 0
Sw1_Value = 0
Sw2_Value = 0
SlidSw_Value = 0
LedRed_Value = 0
LedBlue_Value = 0
LedBuildin_Value = 0
Buzzer_Value = 0


class tiny32_v3:
    def __init__(self):
        self
    
    def Relay(value):
        Relay_Value = Pin(RELAY_PIN, Pin.OUT)
        Relay_Value.value(value)

    def Buzzer_beep(value):
        Buzzer_Value = Pin(BUZZER_PIN, Pin.OUT)

        for j in range(value):
            for i in range(1,50):
                Buzzer_Value.value(1)
                sleep(0.001)
                Buzzer_Value.value(0)
                sleep(0.001)
            sleep(0.1)

    def RedLED(value):
        LedRed_Value = Pin(LED_IO12_PIN, Pin.OUT)
        LedRed_Value.value(value)
                           
     
    def BlueLED(value):
        LedBlue_Value = Pin(LED_IO4_PIN, Pin.OUT)
        LedBlue_Value.value(value)    

    def BuildInLED(value):
        LedBuildin_Value = Pin(LED_BUILDIN, Pin.OUT)
        LedBuildin_Value.value(value) 

    def Sw1():
        Sw1_Value = Pin(SW1_PIN,Pin.IN)
        state = Sw1_Value.value()
        return  not state     
    
    def Sw2():
        Sw2_Value = Pin(SW2_PIN,Pin.IN)
        state = Sw2_Value.value()
        return  not state     
               
    def Slid_Sw():
        SlidSw_Value = Pin(SLID_SW_PIN,Pin.IN)
        state = SlidSw_Value.value()
        return not state     
    
    def header_print():
            print("***********************************************************************")
            print("* Project      :     tiny32_v4_micropython_template")
            print("* Description  :     Template for run tiny32_v4 with Micropython platform")
            print("* Hardware     :     tiny32_v4")
            print("* Author       :     Tenergy Innovation Co., Ltd.")
            print("* Date         :     19/06/2023")
            print(f"* Revision     :     {version}")
            print("* website      :     http://www.tenergyinnovation.co.th")
            print("* Email        :     admin@innovation.co.th")
            print("* TEL          :     +66 82-308-3299")
            print("***********************************************************************/")

               
               


