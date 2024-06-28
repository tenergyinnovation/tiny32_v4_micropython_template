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

    # SW1_PIN = 34
    # SW2_PIN =  35
    # RELAY_PIN =  25
    # LED_IO4_PIN =  4  #blueLED
    # LED_IO12_PIN = 12 #redLED
    # SLID_SW_PIN = 36
    # BUZZER_PIN = 13
    # RXD2_PIN = 16
    # TXD2_PIN = 17
    # Relay_pin = Pin(RELAY, Pin.OUT)
    # RedLED_pin = Pin(LED_IO12, Pin.OUT)
    # BlueLED_pin = Pin(LED_IO4, Pin.OUT)
    # BuildinLED_pin = Pin(2, Pin.OUT)
    # buzzer_beep_pin = Pin(BUZZER, Pin.OUT)
    # Sw1_pin= Pin(SW1, Pin.OUT)
    # Sw2_pin= Pin(SW2, Pin.OUT)
    # Slid_sw_pin= Pin(SLID_SW, Pin.OUT)

    def __init__(self):
        global SW1_PIN
        global SW2_PIN
        global RELAY_PIN
        global LED_IO4_PIN #bludLED
        global LED_IO12_PIN #redLED
        global LED_BUILDIN
        global SLID_SW_PIN
        global BUZZER_PIN
        global RXD2_PIN
        global TXD2_PIN
        global Relay_Value 
        global Sw1_Value 
        global Sw2_Value 
        global SlidSw_Value 
        global LedRed_Value 
        global LedBlue_Value 
        global LedBuildin_Value 
        global Buzzer_Value
        self
    
    def Relay(value):
        global Relay_Value
        global RELAY_PIN
        Relay_Value = Pin(RELAY_PIN, Pin.OUT)
        Relay_Value.value(value)

    def Buzzer_beep(value):
        global BUZZER_PIN
        global Buzzer_Value
        Buzzer_Value = Pin(BUZZER_PIN, Pin.OUT)

        for j in range(value):
            for i in range(1,50):
                Buzzer_Value.value(1)
                sleep(0.001)
                Buzzer_Value.value(0)
                sleep(0.001)
            sleep(0.1)

    def RedLED(value):
        global LedRed_Value
        global LED_IO12_PIN
        LedRed_Value = Pin(LED_IO12_PIN, Pin.OUT)
        LedRed_Value.value(value)
                           
     
    def BlueLED(value):
        global LedBlue_Value
        global LED_IO4_PIN
        LedBlue_Value = Pin(LED_IO4_PIN, Pin.OUT)
        LedBlue_Value.value(value)    

    def BuildInLED(value):
        global LedBuildin_Value
        global LED_BUILDIN
        LedBuildin_Value = Pin(LED_BUILDIN, Pin.OUT)
        LedBuildin_Value.value(value) 

    def Sw1():
        global SW1_PIN
        global Sw1_Value
        Sw1_Value = Pin(SW1_PIN,Pin.IN)
        state = Sw1_Value.value()
        return  not state     
    
    def Sw2():
        global SW2_PIN
        global Sw2_Value
        Sw2_Value = Pin(SW2_PIN,Pin.IN)
        state = Sw2_Value.value()
        return  not state     
               
    def Slid_Sw():
        global SLID_SW_PIN
        global SlidSw_Value
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

               
               


